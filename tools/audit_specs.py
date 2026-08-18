#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, hashlib

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

# 1. JSON syntax
json_files = list(ROOT.rglob("*.json"))
for p in json_files:
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"JSON inválido: {p.relative_to(ROOT)}: {e}")
if not errors:
    ok(f"{len(json_files)} arquivos JSON parseados.")

# 2. Core assets
manifest = load("spec/repo-manifest.json")
lib = load("legal/clause-library.json")
matrix = load("legal/clause-matrix.json")
structure = load("spec/contract-structure.json")
valid = load("tests/cases-valid.json")
invalid = load("tests/cases-invalid.json")
expected = load("tests/expected-clause-sets.json")

if all([lib, matrix, structure]):
    lib_ids = [x["id"] for x in lib["clauses"]]
    matrix_ids = [x["id"] for x in matrix["clauses"]]
    structure_ids = [x["id"] for x in structure["order"]]

    if len(lib_ids) != len(set(lib_ids)):
        err("IDs duplicados em clause-library.")
    else:
        ok("Clause IDs únicos.")

    if set(lib_ids) != set(matrix_ids):
        err(f"Matrix difere da biblioteca: missing={set(lib_ids)-set(matrix_ids)} extra={set(matrix_ids)-set(lib_ids)}")
    else:
        ok("Clause matrix cobre exatamente a biblioteca.")

    if set(lib_ids) != set(structure_ids):
        err(f"Structure difere da biblioteca: missing={set(lib_ids)-set(structure_ids)} extra={set(structure_ids)-set(lib_ids)}")
    else:
        ok("Contract structure cobre exatamente a biblioteca.")

    if len(lib_ids) != len(matrix_ids) or len(lib_ids) != len(structure_ids):
        err("Contagem de cláusulas inconsistente.")

    all_text = "\n".join(x["text"] for x in lib["clauses"])
    for phrase in ["área(s)", "Landing Page(s)", "criativo(s)", "justas e contratadas"]:
        if phrase in all_text:
            err(f"Expressão linguística proibida encontrada: {phrase}")
    if not any("linguística" in e for e in errors):
        ok("Guardas de português canônico aprovadas.")

    placeholders = sorted(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", all_text)))
    if placeholders:
        ok(f"{len(placeholders)} placeholders canônicos encontrados.")
    else:
        warn("Nenhum placeholder encontrado; inesperado.")

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

# 3. Locked legal hashes
hash_file = load("legal/clause-hashes.json")
if lib and hash_file:
    recorded = hash_file.get("clauses", {})
    mismatches = []
    for clause in lib["clauses"]:
        actual = hashlib.sha256(clause["text"].encode("utf-8")).hexdigest()
        if recorded.get(clause["id"]) != actual:
            mismatches.append(clause["id"])

    if mismatches:
        err(f"Clause hashes divergentes: {mismatches}")
    elif set(recorded) != set(x["id"] for x in lib["clauses"]):
        err("Clause hashes não cobrem exatamente a biblioteca.")
    else:
        ok("Clause hashes correspondem exatamente aos textos locked.")

# 4. Valid curated cases
if valid:
    ids = [c["id"] for c in valid["cases"]]
    if len(ids) != len(set(ids)):
        err("IDs duplicados nos casos válidos.")
    else:
        ok(f"{len(ids)} casos válidos únicos.")

    for c in valid["cases"]:
        p = c["payload"]
        exp = c["expected"]
        areas = p["scope"]["areas_count"]
        calc_days = {1: 7, 2: 10, 3: 15}.get(areas)
        if "implementation_business_days" in exp and calc_days != exp["implementation_business_days"]:
            err(f"{c['id']}: prazo esperado inconsistente.")

        total = p["commercial"]["monthly_fee_brl"] * p["term"]["term_months"]
        if "initial_term_reference_value_brl" in exp and abs(total - exp["initial_term_reference_value_brl"]) > 0.001:
            err(f"{c['id']}: valor total esperado inconsistente.")

        signer_count = len(p["individual_contractors"]) if p["contractor_type"] == "PF" else len(p["legal_entity"]["representatives"])
        if "client_signers" in exp and signer_count != exp["client_signers"]:
            err(f"{c['id']}: quantidade de signatários esperada inconsistente.")

# 5. Invalid/manual references
if invalid and valid:
    valid_ids = set(c["id"] for c in valid["cases"])
    bad_refs = []
    for c in invalid["cases"]:
        if c.get("base_fixture") and c["base_fixture"] not in valid_ids:
            bad_refs.append((c["id"], c["base_fixture"]))
    if bad_refs:
        for cid, ref in bad_refs:
            err(f"{cid}: base_fixture inexistente {ref}.")
    else:
        ok(f"{len(invalid['cases'])} casos inválidos/manuais referenciam casos base válidos.")

# 6. Expected clause sets
if expected and valid:
    expected_ids = {c["case_id"] for c in expected["cases"]}
    valid_ids = {c["id"] for c in valid["cases"]}
    if expected_ids != valid_ids:
        err("Expected clause sets não cobrem exatamente os casos válidos.")
    else:
        ok("Expected clause sets cobrem todos os casos válidos.")

# 7. Manifest is authoritative for package completeness
if manifest:
    missing_required = []
    for rel in manifest.get("required_assets", []):
        if not (ROOT / rel).exists():
            missing_required.append(rel)
    if missing_required:
        for rel in missing_required:
            err(f"Required asset ausente segundo repo-manifest: {rel}")
    else:
        ok(f"{len(manifest.get('required_assets', []))} required_assets do repo-manifest presentes.")

# 8. Foundational files not optional
foundational = [
    "AGENTS.md",
    "MASTER_PROMPT.md",
    "START-HERE.md",
    "spec/contract-schema.json",
    "spec/business-rules.json",
    "spec/validation-rules.json",
    "spec/calculation-rules.json",
    "legal/clause-library.json",
    "legal/clause-matrix.json",
    "product/ui-requirements.md",
    "tests/pre-human-gate.md",
]
for rel in foundational:
    if not (ROOT / rel).exists():
        err(f"Arquivo fundamental ausente: {rel}")
if not any("Arquivo fundamental ausente" in e for e in errors):
    ok("Arquivos fundamentais presentes.")

# 9. Known non-blocking brand asset
logo_paths = ["assets/logo-horizontal.svg", "assets/logo-mark.svg", "assets/favicon.svg"]
missing_logo = [x for x in logo_paths if not (ROOT / x).exists()]
if missing_logo:
    warn("Logo oficial não fornecido; fallback tipográfico deve ser usado: " + ", ".join(missing_logo))

print("# SPEC AUDIT")
for level, msg in checks:
    print(f"[{level}] {msg}")
print(f"\nErrors: {len(errors)} | Warnings: {len(warnings)}")
sys.exit(1 if errors else 0)
