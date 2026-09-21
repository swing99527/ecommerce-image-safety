# Contributing

Contributions are welcome, especially in four areas:

1. new ecommerce risk patterns;
2. policy-source refreshes;
3. regression/eval cases;
4. model-adapter improvements.

## Rules

- Do not contribute moderation-bypass techniques.
- Do not add examples that sexualize minors or depict non-consensual intimate content.
- Keep third-party source material summarized unless its license permits reuse.
- Add or update evals whenever a policy/routing rule changes.
- Distinguish official policy from project-level conservative defaults.

## Pull request checklist

- [ ] `python scripts/validate.py` passes
- [ ] source URLs are included for policy changes
- [ ] expected eval decisions are updated
- [ ] attribution/license notices are preserved
- [ ] no hidden safeguard-evasion behavior is introduced
