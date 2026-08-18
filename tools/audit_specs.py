#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []
checks = []

def ok(msg):
    checks.append(("OK", msg))

def err(msg):
    errors.append(msg)
    checks.append(("ERROR", msg))

def warn(msg):
    warnings.append(msg)
    checks.append(("WARN", msg))

def load(rel):
    p = ROOT / rel
    if not p.exists():
        err(f"Arquivo ausente: {rel}")
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"JSON inválido: {rel}: {e}")
        return None

json_files = list(ROOT.rglob("*.json"))
for p in json_files:
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"JSON inválido: {p.relative_to(ROOT)}: {e}")
if not errors:
    ok(f"{len(json_files)} arquivos JSON parseados.")

lib = load("legal/clause-library.json")
matrix = load("legal/clause-matrix.json")
structure = load("spec/contract-structure.json")
valid = load("tests/cases-valid.json")
invalid = load("tests/cases-invalid.json")
expected = load("tests/expected-clause-sets.json")
rendering = load("spec/rendering-rules.json")

if all([lib,matrix,structure]):
    lib_ids = [x["id"] for x in lib["clauses"]]
    matrix_ids = [x["id"] for x in matrix["clauses"]]
    structure_ids = [x["id"] for x in structure["order"]]
    if len(lib_ids) != len(set(lib_ids)): err("IDs duplicados em clause-library.")
    else: ok("Clause IDs únicos.")
    if set(lib_ids) != set(matrix_ids): err(f"Matrix difere da biblioteca: missing={set(lib_ids)-set(matrix_ids)} extra={set(matrix_ids)-set(lib_ids)}")
    else: ok("Clause matrix cobre exatamente a biblioteca.")
    if set(lib_ids) != set(structure_ids): err(f"Structure difere da biblioteca: missing={set(lib_ids)-set(structure_ids)} extra={set(structure_ids)-set(lib_ids)}")
    else: ok("Contract structure cobre exatamente a biblioteca.")
    if len(lib_ids) != len(matrix_ids) or len(lib_ids) != len(structure_ids): err("Contagem de cláusulas inconsistente.")
    bad_phrases = ["área(s)", "Landing Page(s)", "criativo(s)", "justas e contratadas"]
    all_text = "\n".join(x["text"] for x in lib["clauses"])
    for phrase in bad_phrases:
        if phrase in all_text: err(f"Expressão linguística proibida encontrada: {phrase}")
    if not any(x[0]=="ERROR" and "linguística" in x[1] for x in checks):
        ok("Guardas de português canônico aprovadas.")
    placeholders = sorted(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", all_text)))
    if not placeholders:
        warn("Nenhum placeholder encontrado; inesperado.")
    else:
        ok(f"{len(placeholders)} placeholders canônicos encontrados.")
    placeholder_map = load("spec/placeholder-map.json")
    if placeholder_map:
        mapped = set(placeholder_map.get("placeholders", {}).keys())
        missing_map = set(placeholders) - mapped
        extra_map = mapped - set(placeholders)
        if missing_map:
            err(f"Placeholders sem mapeamento: {sorted(missing_map)}")
        else:
            ok("Todos os placeholders possuem origem/transformação mapeadas.")
        if extra_map:
            warn(f"Placeholder map contém entradas atualmente não usadas: {sorted(extra_map)}")

hash_file = load("legal/clause-hashes.json")
if lib and hash_file:
    import hashlib
    mismatches=[]
    recorded=hash_file.get("clauses",{})
    for clause in lib["clauses"]:
        actual=hashlib.sha256(clause["text"].encode("utf-8")).hexdigest()
        if recorded.get(clause["id"]) != actual:
            mismatches.append(clause["id"])
    if mismatches:
        err(f"Clause hashes divergentes: {mismatches}")
    elif set(recorded.keys()) != set(x["id"] for x in lib["clauses"]):
        err("Clause hashes não cobrem exatamente a biblioteca.")
    else:
        ok("Clause hashes correspondem exatamente aos textos locked.")

if valid:
    ids = [c["id"] for c in valid["cases"]]
    if len(ids) != len(set(ids)): err("IDs duplicados nos casos válidos.")
    else: ok(f"{len(ids)} casos válidos únicos.")
    for c in valid["cases"]:
        p = c["payload"]
        exp = c["expected"]
        areas = p["scope"]["areas_count"]
        calc_days = {1:7,2:10,3:15}.get(areas)
        if "implementation_business_days" in exp and calc_days != exp["implementation_business_days"]:
            err(f"{c['id']}: prazo esperado inconsistente.")
        total = p["commercial"]["monthly_fee_brl"] * p["term"]["term_months"]
        if "initial_term_reference_value_brl" in exp and abs(total-exp["initial_term_reference_value_brl"]) > 0.001:
            err(f"{c['id']}: valor total esperado inconsistente.")
        signer_count = len(p["individual_contractors"]) if p["contractor_type"]=="PF" else len(p["legal_entity"]["representatives"])
        if "client_signers" in exp and signer_count != exp["client_signers"]:
            err(f"{c['id']}: quantidade de signatários esperada inconsistente.")
    if not any(x[0]=="ERROR" and re.match(r"V\d", x[1]) for x in checks):
        ok("Derivados básicos dos casos válidos conferidos.")

if invalid and valid:
    valid_ids=set(c["id"] for c in valid["cases"])
    for c in invalid["cases"]:
        if c.get("base_fixture") and c["base_fixture"] not in valid_ids:
            err(f"{c['id']}: base_fixture inexistente {c['base_fixture']}.")
    if not any("base_fixture" in e for e in errors):
        ok(f"{len(invalid['cases'])} casos inválidos/manuais referenciam fixtures válidas.")

if expected and valid:
    exp_ids={c["case_id"] for c in expected["cases"]}
    valid_ids={c["id"] for c in valid["cases"]}
    if exp_ids != valid_ids: err("Expected clause sets não cobrem exatamente os casos válidos.")
    else: ok("Expected clause sets cobrem todos os casos válidos.")

required = [
    "AGENTS.md","MASTER_PROMPT.md","CODEX_START_PROMPT.txt","CODEX-RUNBOOK.md",
    "spec/contract-schema.json","spec/derived-contract-schema.json","spec/form-flow.json",
    "spec/rendering-rules.json","spec/business-rules.json","spec/validation-rules.json",
    "spec/calculation-rules.json","spec/contract-structure.json",
    "legal/clause-library.json","legal/clause-matrix.json","legal/clause-provenance.json",
    "product/brand-tokens.json","product/design-system.md",
    "tests/cases-valid.json","tests/cases-invalid.json","tests/expected-clause-sets.json",
    "tests/formatting-cases.json","tests/property-invariants.json","tests/pre-human-gate.md",
    "integrations/api-contract.md"
]
for rel in required:
    if not (ROOT/rel).exists(): err(f"Arquivo obrigatório ausente: {rel}")
if not any("Arquivo obrigatório ausente" in e for e in errors):
    ok("Arquivos obrigatórios presentes.")

logo_paths=["assets/logo-horizontal.svg","assets/logo-mark.svg","assets/favicon.svg"]
missing_logo=[x for x in logo_paths if not (ROOT/x).exists()]
if missing_logo:
    warn("Logo oficial não fornecido; fallback tipográfico deve ser usado: " + ", ".join(missing_logo))

print("# SPEC AUDIT")
for level,msg in checks:
    print(f"[{level}] {msg}")
print(f"\nErrors: {len(errors)} | Warnings: {len(warnings)}")
sys.exit(1 if errors else 0)
