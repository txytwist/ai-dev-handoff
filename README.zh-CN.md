# AI Dev Handoff

Build software from your phone with ChatGPT, GitHub and Cloud Codex.

面向主要使用 iPhone、没有编程基础的用户。通过文档与模板，把想法、开发任务、实际改动和审核证据留在 GitHub。零运行时依赖，不需要自建服务器、额外付费 API、终端或桌面 IDE。

## 📱 手机上开始

现在只做一件事：[打开首次使用指南](START_HERE.md)。英文首页见 [README](README.md)。

也可把下面短指令连同本仓库可访问链接（不能读取时粘贴文档内容）发给 ChatGPT：

```text
我想使用 AI Dev Handoff。请读取我提供的 README、START_HERE.md 和 CHATGPT_SETUP.md。
先问我创建新项目还是接入已有项目，一次只给一个必要操作。
先核实你能读取和写入什么；不要假装只凭项目名就加载了规范。
先规划，等我批准范围后再交给 Codex。
```

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

[维护与校验](CONTRIBUTING.md) · [安全](SECURITY.md) · [许可证待定](LICENSE_PENDING.md)。当前仓库保持私有，公开与许可由所有者决定。
