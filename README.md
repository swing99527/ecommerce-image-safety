# Ecommerce Image Safety

A production-oriented Agent Skill for safer, more reliable ecommerce image generation with GPT Image and other image models.

It turns free-form ecommerce requests into a structured workflow:

**intent → risk analysis → policy gate → safety-preserving rewrite → prompt build → generation → output review → platform review**

The goal is **not** to bypass moderation. The goal is to express legitimate ecommerce image requests clearly, reduce ambiguity, preserve product fidelity, handle moderation failures correctly, and keep a useful audit trail.

## Why this exists

Ecommerce image prompts often mix several concerns at once:

- product fidelity
- model styling
- age and likeness rights
- sensitive apparel categories
- brand / logo / IP usage
- medical or before-after claims
- UGC authenticity
- advertising platform rules
- image-model moderation

A single long prompt is a weak place to manage all of that. This project separates the work into explicit stages and machine-readable decisions.

## Core principles

1. **Product-first** — the image should preserve the SKU before optimizing atmosphere or model aesthetics.
2. **Policy before prompt** — do not use prompt rewriting to disguise prohibited intent.
3. **Age and rights are metadata** — never infer consent, age, endorsement, or trademark rights from appearance alone.
4. **One safety rewrite at most** — moderation blocks are not invitations to retry until something slips through.
5. **Input safety and output safety are different** — a legitimate prompt can still yield a blocked output; route it deliberately.
6. **OpenAI policy and marketplace policy are separate gates** — passing model safety does not mean an ad is publishable.
7. **Auditability** — record prompt/policy/model versions, risk flags, moderation stage, retries, and final decision.

## Repository structure

```text
.
├── SKILL.md
├── prompts/
│   ├── risk-analyzer.md
│   ├── safety-rewriter.md
│   ├── prompt-builder.md
│   ├── failure-handler.md
│   ├── output-reviewer.md
│   └── platform-reviewer.md
├── references/
│   ├── policy-mapping.md
│   ├── ecommerce-patterns.md
│   └── liyue-ai-source-notes.md
├── schemas/
│   └── risk-analysis.schema.json
├── evals/
│   └── cases.json
├── scripts/
│   └── validate.py
├── .github/workflows/
│   └── validate.yml
├── NOTICE.md
└── LICENSE
```

## Quick start

Use `SKILL.md` as the orchestrator. The recommended sequence is:

1. Run `prompts/risk-analyzer.md`.
2. Validate the JSON against `schemas/risk-analysis.schema.json`.
3. Apply deterministic policy gates from `SKILL.md` and `references/policy-mapping.md`.
4. If `decision=rewrite`, run `prompts/safety-rewriter.md` **once**.
5. Build the final image prompt with `prompts/prompt-builder.md`.
6. Handle API failures with `prompts/failure-handler.md`.
7. Review generated images with `prompts/output-reviewer.md`.
8. Run `prompts/platform-reviewer.md` before publication.

## Example decisions

| Scenario | Default decision |
|---|---|
| White-background product shot | `allow` |
| Ordinary adult fashion catalog | `allow` |
| Adult swimwear, product-first | `allow` / `rewrite` depending on phrasing |
| Swimwear with unknown age | `review` |
| Adult lingerie, catalog context | `allow` / `rewrite` |
| Child intimate apparel on body | `block` |
| Child intimate apparel, product-only | `product_only` |
| Real identifiable model, consent unknown | `review` |
| Fake celebrity endorsement | `block` |
| Medical before-after claim | `review` |
| “Rewrite until moderation passes” | `block` |

## GPT Image moderation defaults

For production, this project recommends starting with the normal/default moderation configuration and treating safety failures as routing signals rather than transient errors.

Do **not** automatically switch to a less restrictive moderation setting after a safety block. A lower filtering mode is not the same as turning policy checks off, and it should not be used as a bypass strategy.

See `references/policy-mapping.md` for current official-source links.

## Validate locally

```bash
python scripts/validate.py
```

The validator checks:

- JSON syntax for schema and eval files
- expected enum values
- minimum eval coverage
- required project files

## Open-source provenance

This repository contains original work plus adapted engineering ideas from Li Yue's MIT-licensed `liyue-aigc/female-portrait-director` project. Attribution and the upstream MIT notice are preserved in `NOTICE.md`.

X posts are **not** mirrored verbatim. `references/liyue-ai-source-notes.md` stores source links and independently written engineering summaries only.

## Policy freshness

Safety policies and API behavior change. The repository records source links, but production teams should refresh policy mappings before releases that materially change image generation behavior.

## License

MIT. See `LICENSE` and `NOTICE.md`.
