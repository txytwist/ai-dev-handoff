# AI Dev Handoff

Build software from your phone with ChatGPT, GitHub and Cloud Codex.

**Public Beta 准备阶段。最近核实（2026-11-20）仍为 Private；所有者改为 Public 后即为公开可读测试版，以 GitHub 实际状态为准。许可证仍待决定，公开可读不等于授予开源许可。**

面向主要使用 iPhone、没有编程基础的用户。通过文档与模板，把想法、开发任务、实际改动和审核证据留在 GitHub。零运行时依赖，不需要自建服务器、额外付费 API、终端或桌面 IDE。

## 📱 手机上开始

现在只做一件事：[打开首次使用指南](START_HERE.md)。英文首页见 [README](README.md)。

## 角色分工一眼看懂

这是典型手动场景的说明性对比，不代表所有工作流，也不是实测效果。[查看两张流程图与权限说明](docs/workflow.md)。

| 角色 | 无统一交接流程（常见手动方式） | 使用 AI Dev Handoff |
| --- | --- | --- |
| 👤 用户 | 在多个对话间整理上下文、传递信息并追踪结果 | 提目标、批范围、主动交接；决定验收与合并 |
| 🧠 ChatGPT | 临时建议；任务和审核依据可能留在聊天里 | 规划范围与验收；权限允许时创建 Issue；依据真实 PR 证据审核 |
| 📦 GitHub | 常保存代码，任务上下文可能分散 | 在用户自己的项目仓库保存 Issue、规范、任务、PR、交接与审核证据 |
| 💻 Cloud Codex | 每轮可能需重新解释需求 | 读取可访问的 Issue / `docs/tasks/` 与规范，开发、测试、提交 PR/交接 |
| 🔄 协作 | 手动传话与临时记忆 | 可追踪的规划 → 用户批准 → 执行 → 审核 → 用户决策 |

## 复制初始化指令

首次使用推荐复制 [完整引导块](docs/portable-starter.md)，无需再逐一打开模板。没有框架私有访问权限时，由所有者在授权范围内提供该块全文；收到之前不承诺可以安装。

短入口指令（读不到链接时需提供上面的完整引导块）：

```text
我想使用 AI Dev Handoff。未来公共入口是 https://github.com/txytwist/ai-dev-handoff ，先确认实际可见性：Private 时需授权访问或引导全文，Public 时为公开测试版，许可仍待决定。
有授权访问时，读取所有者提供的审核分支 START_HERE.md 和 CHATGPT_SETUP.md；读不到就请提供 portable-starter 完整引导块，不假装已加载。
先问我新项目还是已有项目，一次只给一个必要操作。
```

所有者单独决定 Public 后，再用无私有权限的手机验证外部入口。许可可以继续待定，但不能宣称已开源授权；Private 时不能把 URL 当作已可用公共入口。详见 [实机待办与公开门槛](docs/mobile-acceptance.md)。

外部 AI 测试：复制 [一次式评审提示](docs/external-ai-test.md)，按矩阵报告证据。反馈见 [贡献指南](CONTRIBUTING.md)，不要提交秘密或保密项目。

## 每天只记三句话

ChatGPT 提想法。Codex 执行。ChatGPT 审核。

你先与 ChatGPT 确定目标和验收条件，同意后优先由 ChatGPT 在**你的项目仓库**创建 Issue。你打开 Cloud Codex 并明确授权执行指定任务。Codex 提交 PR 和交接记录后，你主动回到 ChatGPT 提供链接。ChatGPT 核实实际改动与测试，你决定接受、要求修改或继续下一轮。

## 两种开始方式

新项目：ChatGPT 先核实建仓能力和授权；不足时你在手机 GitHub 网页创建一次 Private 仓库，再授权连接访问。只初始化最小必要文件，不需要 Fork 整个框架。

已有项目：ChatGPT 先读取目录和已有规则，提出接入计划；批准后只合并必要规则和交接目录，不覆盖已有程序或 AGENTS.md。详见 [两种模式步骤](START_HERE.md)。

`txytwist/ai-dev-handoff` 是框架仓库；日常任务属于你自己的项目仓库，可以在多个项目分别使用。

## 权限不足也能交接

- ChatGPT 不能写 Issue：生成完整任务，由你交给 Codex，先保存到项目 `docs/tasks/` 再执行。
- Codex 不能读 Issue：你提供任务全文或可读的版本化任务文件；先确认读到了正确任务。
- ChatGPT 不能读取 PR：提供文件、完整 diff、提交标识和测试输出。它只能审核提供的材料，应写明未核实部分，不能声称已读远端 PR。
- Codex 无法推送或创建 PR：保留提交和交接记录，明确阻塞；你在手机 GitHub 网页从功能分支创建 PR。未推送时不能声称 GitHub 已有代码。

## 继续阅读

[初始化指令](CHATGPT_SETUP.md) · [Codex 指令](CODEX_SETUP.md) · [日常速查](docs/mobile-quickstart.md) · [完整状态闭环](docs/workflow.md) · [示例](examples/complete-cycle.md)

PR 是待审核的变更提案；分支是独立修改空间；Handoff 是说明做了什么和证据在哪的交接记录。审核意见不等于合并授权。合并、部署、发布、删数据、公开仓库都需要用户单独决定。工具不会自动共享聊天或自动唤醒对方。

账户套餐、GitHub 授权与 Cloud Codex 可用性取决于个人账户。本项目未实测 iPhone 界面或所有套餐，不保证固定按钮名称；基础使用不依赖 Skill/Plugin 安装。只输入项目名不会自动读取规范。

[维护与校验](CONTRIBUTING.md) · [安全](SECURITY.md) · [许可证待定](LICENSE_PENDING.md)。公开与许可由所有者分别决定；状态以 GitHub 实际可见性为准。
