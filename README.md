# AI Dev Handoff

Build software from your phone with ChatGPT, GitHub and Cloud Codex.

Mobile-First · Beginner-Friendly · Human-in-the-Loop · GitHub-Native

**Public Beta preparation.** Private at the last verified check (2026-11-20). After the owner changes visibility, this becomes a publicly readable beta; check the live GitHub state. License remains pending: public access is not an open-source license.

For beginners who mainly use an iPhone. This is a documentation and template workflow with zero runtime dependencies, not a hosted app.

## 📱 Start on iPhone

[Open the phone setup guide](START_HERE.md) · [完整中文说明](README.zh-CN.md)

For internal testing, copy the entire self-contained block in [the portable starter](docs/portable-starter.md). If you cannot open this private repository, ask the owner to provide that full block within authorized sharing scope. A project name alone cannot load instructions.

Short entry prompt (the full block above is the fallback when links cannot be read):

```text
I want to use AI Dev Handoff. Candidate public entry: https://github.com/txytwist/ai-dev-handoff .
Check actual visibility first: Private requires authorized access or the full starter text; Public means a beta available for review, with license pending.
If authorized access works, read START_HERE.md and CHATGPT_SETUP.md from the review branch supplied by the owner; otherwise ask for the full portable starter text, never claim to have loaded it.
First ask: new project or existing project? Give one necessary action at a time.
```

After the owner explicitly changes visibility for beta testing, verify that an outside iPhone user can obtain the complete starter at that URL without private access. Until then, external onboarding is pending. See [acceptance gates](docs/mobile-acceptance.md).

[External AI reviewers: copy one prompt and run the test matrix](docs/external-ai-test.md). Report reproducible findings through [feedback guidance](CONTRIBUTING.md); never post confidential material.

Plan in ChatGPT. Execute in Cloud Codex. Review in ChatGPT.

## What you get

- [Phone setup, new and existing projects](START_HERE.md)
- [ChatGPT initializer and review prompt](CHATGPT_SETUP.md)
- [Two Cloud Codex execution prompts](CODEX_SETUP.md)
- [Workflow and status definitions](docs/workflow.md)
- [Daily phone quickstart](docs/mobile-quickstart.md)
- [Complete example cycle](examples/complete-cycle.md)
- [Reusable project context](templates/PROJECT_CONTEXT.md), [agent rules](templates/AGENTS.md), [task](templates/TASK_TEMPLATE.md), [handoff](templates/HANDOFF_TEMPLATE.md), [review](templates/REVIEW_TEMPLATE.md)

## Limits and decisions

ChatGPT, GitHub and Cloud Codex access depends on your account entitlements and repository permissions. Issue access in Codex must be verified. Chats do not automatically sync or wake each other. The user returns to ChatGPT with the PR and handoff. Review is not permission to merge, deploy, publish, delete data or make a repository public.

Use these templates in **your own project repository**; no fork of this framework is needed. Multiple projects can reuse them independently. When GitHub writes are unavailable, use a copied task saved by Codex in `docs/tasks/` before execution. When reads are unavailable, supply files and diffs; review remains limited to the evidence supplied.

## Validation and contribution

Maintainers run `python3 scripts/validate.py` offline; phone users do not need a terminal or local environment. This checks documentation structure, links and common secret patterns, not platform UI or all possible secrets. See [contribution guidance](CONTRIBUTING.md) and [security](SECURITY.md).

License choice is pending; see [LICENSE_PENDING.md](LICENSE_PENDING.md). The owner alone decides visibility. Public visibility does not grant a software license.
