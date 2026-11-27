# 📱 手机上开始：只做当前一步

**Public Beta（公开测试中，许可证未确定，实机验收未完成）。** 框架仓库已公开；阅读引导不需登录、私有权限或 Fork。你的业务仓库仍建议默认 Private。

直接打开 [完整引导](docs/portable-starter.md) 并复制全文。ChatGPT 或 Gemini 读不到公开链接时，你粘贴全文即可，不必找所有者取材料。入口：https://github.com/txytwist/ai-dev-handoff 。

外部 AI 评审使用 [独立提示与测试矩阵](docs/external-ai-test.md)，真实手机视觉验收看 [极简检查单](docs/mobile-acceptance.md)，当前状态见 [Beta说明](docs/public-beta.md)。

统一交接让规划、执行、记录与审核分工清楚，用户仍掌握决策权。

## 现在只做这一件事

复制 [完整引导副本](docs/portable-starter.md) 中唯一的文本块到 ChatGPT 或 Gemini。若AI打不开链接，请在手机浏览器打开公开引导页，复制文本块给它；若页面本身访问失败，记录阻塞，不假称已读取。它会先问你“新项目还是已有项目”，再逐步带你走。不要一次执行下面所有行；表格是你随时确认位置的路线图。

访问条件：手机能使用规划端（ChatGPT 或 Gemini）、GitHub 和执行端（Cloud Codex 或 Antigravity）；套餐、连接授权与额度依账户而定。不需要终端、SSH、电脑、自建服务器或额外 API。iPhone UI 未实测，以下按功能描述，不承诺按钮名。

## A：新项目，一次一步

| 当前一步 | 完成标志 | 下一步 |
| --- | --- | --- |
| 1 把引导块发给 ChatGPT/Gemini，选择新项目、说目标 | 规划端复述目标，只问一个必要问题 | 2 |
| 2 让规划端核实建仓、读取、写 Issue、写文件能力及你的授权 | 已知能做什么；权限不能互推 | 3 |
| 3 建一次独立 Private 仓库 | 有自己的仓库 URL，包含初始 README；规划端/执行端连接能访问它 | 4 |
| 4 让规划端提出最小初始化文件计划，并批准范围 | AGENTS.md、PROJECT_CONTEXT.md、NEXT_TASK.md，以及默认的两份Skill与许可；首个小任务及验收已明确 | 5 |
| 5 规划端优先创建 Issue；无写权限则给完整任务 | 有真实 Issue URL，或可复制的完整批准任务 | 6 |
| 6 打开 Cloud Codex 或绑定自己仓库的 Antigravity Project，粘贴任务并授权执行 | 执行端复述正确仓库与任务，更新NEXT_TASK.md，在功能分支提交初始化文件与小任务的一个 PR、Handoff | 7 |
| 7 主动回 ChatGPT/Gemini，给 PR、提交与交接 | 审核端已读实际 diff/证据，或明确缺失材料；给审核意见 | 8 |
| 8 决定接受或返工 | 决定已记录；返工经批准再交执行端，回 7 | 新需求重新规划 |

第 3 步：有能力且有授权时由规划端建仓；已知没有能力则你在手机打开 https://github.com/new ，选自己账号、填项目名、选择 Private、添加 README，创建一次，然后授权连接访问。**不把已知失败转给执行端重试。**

第 6 步默认由 **执行端（Codex 或 Antigravity）提交初始化文件**，与第一个小任务一起审核，**不要求额外初始化 PR 或提前合并**。Antigravity 必须优先从绑定目标 GitHub 仓库的 **Project** 内发起会话以具备推送和建 PR 权限。若你选择只做初始化，则它本身是单独 PR；用户审核并单独决定是否合并后，再从最新基线开始业务任务。规划端有写文件能力时也只能在获准范围提交分支，不能直接写 main。

## B：已有项目，一次一步

| 当前一步 | 完成标志 | 下一步 |
| --- | --- | --- |
| 1 发引导块，选择已有项目，给自己的仓库 URL | 目标仓库正确，规划端确认真实读取能力 | 2 |
| 2 让它读目录、README、AGENTS.md 与上下文 | 回报实际 ref/路径（遇 MCP 单文件无正文先走 diff 降级）；无法完整还原就请你提供材料 | 3 |
| 3 查看接入计划并批准 | 仅补缺失文件/合并必要规则；不覆盖已有规范或程序 | 4 |
| 4 规划端优先建接入 Issue，失败则给完整任务 | 有真实任务与批准证据 | 5 |
| 5 执行端选自己的仓库执行接入（Antigravity 从绑定仓库的 Project 发起） | 核验状态滞后并保存任务，原分支之外的功能分支提交接入 PR/Handoff；现有代码与规则变动可核对 | 6 |
| 6 主动回 ChatGPT/Gemini 审核，决定接受或返工 | 无覆盖证据和用户决定已记录 | 7 |
| 7 用户单独决定是否合并接入 PR | 已合并才以新 main 开始下一任务；未合并则暂停或明确后续基线 | 日常三步 |

默认由执行端提交接入文件。框架仓库不是业务项目，不需 Fork；已有 AGENTS.md 合并条款，不整份替换。接入 PR 不自动合并。

## 卡住时

规划端不能写 Issue → 给完整任务，执行端先存NEXT_TASK.md 再实施。执行端不能读 Issue → 你贴全文或版本化任务。GitHub MCP 单文件 `get_file_contents` 无正文 → 先列举目录并用 `get_commit(detail="full_patch")` 或 `pull_request_read(method="get_diff")` 还原近期全文；历史文件局部 diff 无法 100% 还原时报告阻塞并请你补全文，禁止猜测。审核端不能读 PR → 你提供完整 diff、文件、ref 和日志，只能审核提供的快照。不能推送或建 PR → 报告阻塞，不声称 GitHub 已交付（若 Antigravity 普通会话未绑定 Project 导致推送返回 HTTP 403，可导出 `git format-patch` 附 SHA256 上传 Google Drive，再从绑定目标仓库的 Project 会话校验后用 `git am` 无损恢复推送）。

## 设置一次，日常三步

项目建立后，可把引导规则保存到 ChatGPT Project 或 Gemini Gem 的项目指令；没有此功能时新对话重贴规则和最新上下文，不承诺自动记忆。权威规范在自己的项目仓库，每次先确认读到正确 ref 并交叉核验 `main` 与 `NEXT_TASK.md` 是否滞后。

规划端（ChatGPT / Gemini）提想法 → 执行端（Cloud Codex / Antigravity）执行 → 规划端审核。用户主动来回传递；审核不等于合并、部署或公开授权。进一步说明见 [详细初始化规则](CHATGPT_SETUP.md)，但首次引导全文已足够开始，无须跳转所有文档。

## 新项目默认继承两份仓库 Skill

新项目初始化默认包含 `.agents/skills/` 完整固定包（caveman、ponytail、manifest及许可），无需另行勾选。只有用户明确禁用时跳过对应Skill并记录；现有规范/文件仍不得覆盖。每次新会话先按AGENTS主动读取并执行两份Skill，失败必须报告；严格区分 Codex 原生 `skills/list` 接口与 Antigravity 自身的 Skill 发现机制（不得因缺少 Codex CLI 断言不支持原生 Skill；无宿主发现机制的环境如纯对话端 Gemini 读取全文后须标记“按文件指令执行”，不冒充原生激活）。初始化脚本、禁用方式与四级证据见 [Skill说明](docs/cloud-skills.md)。这不是手机端安装或新云端会话自动激活已经实测的承诺。
