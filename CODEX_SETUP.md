# Cloud Codex / Antigravity 执行指令

在手机或云端工作区打开 Cloud Codex 或 Antigravity，选择或连接**用户项目仓库**，确认名称后粘贴其中一种。尖括号内容由规划端（ChatGPT 或 Gemini）填好再交给你。平台能否读 Issue 必须现场核实；选择仓库不代表自动具备 Issue API 访问。

## A：指定 Issue

```text
目标仓库：<owner/repo>。请读取 Issue <完整链接和编号>，包括评论，先读AGENTS.md、NEXT_TASK.md（如存在）及当前PR，再读PROJECT_CONTEXT.md与相关规范；同时交叉核验当前 main 最新提交与 NEXT_TASK.md 所列 PR 合并状态是否一致（若 PR 已合并仍标 REVIEW，报告滞后并以真实 main 为准）。
每次新会话按AGENTS主动读取并执行caveman和ponytail；仅用户明确禁用的Skill跳过，加载失败报告Skill/路径/原因。无原生skills/list的宿主（如Antigravity）读全文后标明“按文件指令执行”，不冒充原生激活，并在交接中按原生发现、正文读取、按文件指令执行、新会话自动激活四级记录。
先确认仓库、当前 main/默认分支、工作区状态与实际读取的 Issue 标题和要求。读不到 Issue 就停止依赖该内容的执行，要求完整任务正文或版本化NEXT_TASK.md（已有docs/tasks/历史文件也可读），不要猜测。
本次批准的范围及批准证据：<用户同意的范围/消息或任务记录>。若任务仍 PLANNED 或批准不明确，先请求确认。
从最新基线创建独立功能分支，只在此仓库按批准范围实施。在NEXT_TASK.md记录状态IN_PROGRESS及任务来源（同步收敛合并前的旧滞后状态）；完整需求和批准证据留Issue/PR。
运行适用测试与检查，记录实际命令、结果和未运行项；不要把未运行写为通过。
提交PR并在PR记录任务、基线/分支、验证提交、改动、命令结果、四级Skill证据与限制。日常只更新NEXT_TASK.md：状态REVIEW、PR或分支、验证结果、未测项、下一步唯一任务、阻塞；仅里程碑归档docs/handoff/。
不能推送或建 PR时保留提交并报告确切阻塞，不伪造链接。不要自行合并、部署、公开仓库或修改其他项目。完成后等待用户回 ChatGPT 或 Gemini 审核，不自动唤醒它。
```

## B：规划端不能写 Issue／执行端不能读 Issue

```text
目标仓库：<owner/repo>。下面是经我批准的完整任务（或读取NEXT_TASK.md中的任务；已有docs/tasks/也可作为来源）：
<粘贴 TASK_TEMPLATE 的完整内容，含范围、验收、批准证据；若来自不可读 Issue，保留其链接并注明内容由用户提供>
先读取AGENTS.md、NEXT_TASK.md（如存在）、当前Issue/PR与仓库现状，再读PROJECT_CONTEXT.md，交叉核验main最新提交与NEXT_TASK.md状态是否滞后，确认任务与实际权限；每次新会话主动读取并执行两份Skill，仅明确禁用时跳过，加载失败报告并按四级证据区分原生发现与按文件指令执行。没有完整任务或批准证据时先澄清。
从最新基线创建功能分支，无法读取/写入Issue时先把完整任务和批准依据保存在NEXT_TASK.md，再实施、运行适用测试并如实记录。
遵守 A 指令相同的范围、安全与提交要求：任务 IN_PROGRESS → REVIEW，代码和任务一起保存在 GitHub，详情写在PR，日常只更新NEXT_TASK.md六项状态字段，仅里程碑归档docs/handoff/。
PR 创建后补回交接链接；不能推送/创建时说明阻塞，不声称完成远端交付。不得合并、发布、部署、公开或修改其他项目；等待用户返回 ChatGPT 或 Gemini 审核。
```

可复用 [任务](templates/TASK_TEMPLATE.md) 与 [交接](templates/HANDOFF_TEMPLATE.md)。

## 新项目默认 Skill 初始化

新项目批准初始化后默认创建最小规范、上下文、NEXT_TASK.md，并完整继承 [固定技能包](docs/cloud-skills.md)，不需额外请求；只有用户明确禁用时才跳过并记录。已有项目不覆盖规范或Skill，先报告冲突。原开发、测试、安全、授权、PR与Handoff要求全部保留。
