#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "SKILL.md",
    "LICENSE",
    "NOTICE.md",
    "prompts/risk-analyzer.md",
    "prompts/safety-rewriter.md",
    "prompts/prompt-builder.md",
    "prompts/failure-handler.md",
    "prompts/output-reviewer.md",
    "prompts/platform-reviewer.md",
    "references/policy-mapping.md",
    "references/ecommerce-patterns.md",
    "references/liyue-ai-source-notes.md",
    "schemas/risk-analysis.schema.json",
    "evals/cases.json",
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("Missing required files:")
    for p in missing:
        print(" -", p)
    sys.exit(1)

schema = json.loads((ROOT / "schemas/risk-analysis.schema.json").read_text())
cases = json.loads((ROOT / "evals/cases.json").read_text())

allowed_decisions = {"allow", "rewrite", "review", "product_only", "block"}
for item in cases:
    if item.get("expected") not in allowed_decisions:
        raise SystemExit(f"Invalid expected decision: {item}")

if len(cases) < 30:
    raise SystemExit(f"Expected >=30 eval cases, got {len(cases)}")

schema_decisions = set(schema["properties"]["decision"]["enum"])
if schema_decisions != allowed_decisions:
    raise SystemExit(f"Schema decision enum mismatch: {schema_decisions}")

print(f"OK: {len(cases)} eval cases; schema JSON valid; required files present")
