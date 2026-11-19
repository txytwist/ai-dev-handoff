# AI Dev Handoff

Build software from your phone with ChatGPT, GitHub and Cloud Codex.

Mobile-First · Beginner-Friendly · Human-in-the-Loop · GitHub-Native

For beginners who mainly use an iPhone. This is a documentation and template workflow with zero runtime dependencies, not a hosted app.

## 📱 Start on iPhone

[Open the phone setup guide](START_HERE.md) · [完整中文说明](README.zh-CN.md)

Copy this into ChatGPT to begin (provide the accessible README or paste its contents):

```text
I want to use AI Dev Handoff. Read the README and CHATGPT_SETUP.md I provide.
First ask whether I want a new project or to add this workflow to an existing project.
Give me one necessary action at a time. Verify access before claiming to read or write GitHub.
Plan first and wait for my approval before execution.
```

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

License choice is pending; see [LICENSE_PENDING.md](LICENSE_PENDING.md). The repository stays private until the owner explicitly decides otherwise.
