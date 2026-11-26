# AI Dev Handoff

Build software from your phone with ChatGPT or Gemini, GitHub, and Cloud Codex or Antigravity.

## 📱 Start on iPhone

[Copy the complete starter](docs/portable-starter.md) · [Step-by-step setup](START_HERE.md) · [中文](README.zh-CN.md)

**Public Beta — license pending; real iPhone acceptance not completed.** The framework is public. No login, private-repo permission or fork is needed to read this guide. Your own project can stay Private.

Copy the starter's single text block into ChatGPT or Gemini. If the AI cannot read the public link, paste the full block yourself; you do not need to ask the owner for public instructions. A project name alone does not load rules.

For beginners who mainly use an iPhone. A documentation/template workflow with zero runtime dependencies, not a hosted app.

Plan in ChatGPT or Gemini. Execute in Cloud Codex or Antigravity. Review in ChatGPT or Gemini.

## Roles at a glance

Illustrative manual scenario, not a universal claim or measured benefit. Short role sections replace a wide table. [Flow diagrams and permission details](docs/workflow.md).

### 👤 User

- **Without:** Copies context across chats and tracks results.
- **With:** Sets goals, approves scope, initiates handoffs; decides acceptance and merge.

### 🧠 ChatGPT / Gemini

- **Without:** Ad hoc advice; task and review context may stay in chat.
- **With:** Plans scope and acceptance; creates Issues when permitted; reviews actual PR evidence.

### 📦 GitHub

- **Without:** Often stores code while context may be scattered.
- **With:** Keeps Issues, rules, tasks, PRs, handoffs and review evidence in the user's own project.

### 💻 Cloud Codex / Antigravity

- **Without:** May need requirements re-explained each round.
- **With:** Reads accessible Issues / `NEXT_TASK.md` and rules; implements, tests, submits PR/handoff.

### 🔄 Collaboration

- **Without:** Manual messages and informal memory.
- **With:** Traceable plan → user approval → execution → review → user decision.

[External AI review prompt](docs/external-ai-test.md) · [Feedback](CONTRIBUTING.md) · [iPhone checks still to run](docs/mobile-acceptance.md)

## What you get

- [Phone setup, new and existing projects](START_HERE.md)
- [ChatGPT / Gemini initializer and review prompt](CHATGPT_SETUP.md)
- [Cloud Codex / Antigravity execution prompts](CODEX_SETUP.md)
- [Workflow and status definitions](docs/workflow.md)
- [Daily phone quickstart](docs/mobile-quickstart.md)
- [Complete example cycle](examples/complete-cycle.md)
- [Reusable project context](templates/PROJECT_CONTEXT.md), [agent rules](templates/AGENTS.md), [task](templates/TASK_TEMPLATE.md), [handoff](templates/HANDOFF_TEMPLATE.md), [review](templates/REVIEW_TEMPLATE.md)

## Limits and decisions

ChatGPT/Gemini, GitHub and Cloud Codex/Antigravity access depends on your account entitlements and repository permissions. Issue access in the executor must be verified. Chats do not automatically sync or wake each other. The user returns to ChatGPT or Gemini with the PR and handoff. Review is not permission to merge, deploy, publish, delete data or make a repository public.

Use these templates in **your own project repository**; no fork of this framework is needed. Multiple projects can reuse them independently. When GitHub writes are unavailable, use a copied task saved by Codex or Antigravity in `NEXT_TASK.md` before execution. When direct single-file MCP reads fail, fall back to full commit/PR diffs or user-supplied files; review remains limited to the evidence verified.

## Validation and contribution

Maintainers run `python3 scripts/validate.py` offline; phone users do not need a terminal or local environment. This checks documentation structure, links and common secret patterns, not platform UI or all possible secrets. See [contribution guidance](CONTRIBUTING.md) and [security](SECURITY.md).

License choice is pending; see [LICENSE_PENDING.md](LICENSE_PENDING.md). The owner alone decides visibility. Public visibility does not grant a software license.
