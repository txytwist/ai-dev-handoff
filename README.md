# AI Dev Handoff

Build software from your phone with ChatGPT, GitHub and Cloud Codex.

## 📱 Start on iPhone

[Copy the complete starter](docs/portable-starter.md) · [Step-by-step setup](START_HERE.md) · [中文](README.zh-CN.md)

**Public Beta — license pending; real iPhone acceptance not completed.** The framework is public. No login, private-repo permission or fork is needed to read this guide. Your own project can stay Private.

Copy the starter's single text block into ChatGPT. If the AI cannot read the public link, paste the full block yourself; you do not need to ask the owner for public instructions. A project name alone does not load rules.

For beginners who mainly use an iPhone. A documentation/template workflow with zero runtime dependencies, not a hosted app.

Plan in ChatGPT. Execute in Cloud Codex. Review in ChatGPT.

## Roles at a glance

Illustrative manual scenario, not a universal claim or measured benefit. Short role sections replace a wide table. [Flow diagrams and permission details](docs/workflow.md).

### 👤 User

- **Without:** Copies context across chats and tracks results.
- **With:** Sets goals, approves scope, initiates handoffs; decides acceptance and merge.

### 🧠 ChatGPT

- **Without:** Ad hoc advice; task and review context may stay in chat.
- **With:** Plans scope and acceptance; creates Issues when permitted; reviews actual PR evidence.

### 📦 GitHub

- **Without:** Often stores code while context may be scattered.
- **With:** Keeps Issues, rules, tasks, PRs, handoffs and review evidence in the user's own project.

### 💻 Cloud Codex

- **Without:** May need requirements re-explained each round.
- **With:** Reads accessible Issues / `NEXT_TASK.md` and rules; implements, tests, submits PR/handoff.

### 🔄 Collaboration

- **Without:** Manual messages and informal memory.
- **With:** Traceable plan → user approval → execution → review → user decision.

[External AI review prompt](docs/external-ai-test.md) · [Feedback](CONTRIBUTING.md) · [iPhone checks still to run](docs/mobile-acceptance.md)

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

Use these templates in **your own project repository**; no fork of this framework is needed. Multiple projects can reuse them independently. When GitHub writes are unavailable, use a copied task saved by Codex in `NEXT_TASK.md` before execution. When reads are unavailable, supply files and diffs; review remains limited to the evidence supplied.

## Validation and contribution

Maintainers run `python3 scripts/validate.py` offline; phone users do not need a terminal or local environment. This checks documentation structure, links and common secret patterns, not platform UI or all possible secrets. See [contribution guidance](CONTRIBUTING.md) and [security](SECURITY.md).

License choice is pending; see [LICENSE_PENDING.md](LICENSE_PENDING.md). The owner alone decides visibility. Public visibility does not grant a software license.
