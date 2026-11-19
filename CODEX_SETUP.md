# Cloud Codex 执行指令

在手机打开 Cloud Codex，选择**用户项目仓库**，确认名称后粘贴其中一种。尖括号内容由 ChatGPT 填好再交给你。平台能否读 Issue 必须现场核实；选择仓库不代表自动具备 Issue API 访问。

## A：指定 Issue

```text
目标仓库：<owner/repo>。请读取 Issue <完整链接和编号>，包括评论，及该仓库 AGENTS.md、PROJECT_CONTEXT.md 与相关规范。
先确认仓库、当前 main/默认分支、工作区状态与实际读取的 Issue 标题和要求。读不到 Issue 就停止依赖该内容的执行，要求完整任务正文或版本化 docs/tasks/ 文件，不要猜测。
本次批准的范围及批准证据：<用户同意的范围/消息或任务记录>。若任务仍 PLANNED 或批准不明确，先请求确认。
从最新基线创建独立功能分支，只在此仓库按批准范围实施。把任务与来源/批准记录保存到 docs/tasks/<任务名>.md，状态 IN_PROGRESS。
运行适用测试与检查，记录实际命令、结果和未运行项；不要把未运行写为通过。
提交变更，更新任务为 REVIEW，保存 docs/handoff/<任务名>.md，含任务/PR/路径、基线与分支、被验证提交、改动清单、证据、限制和下一步。创建 PR 并把链接补回交接；交接文件不写自身提交 SHA，最终 head 在 PR/最终回复中给出。
不能推送或建 PR时保留提交并报告确切阻塞，不伪造链接。不要自行合并、部署、公开仓库或修改其他项目。完成后等待用户回 ChatGPT 审核，不自动唤醒它。
```

## B：ChatGPT 不能写 Issue／Codex 不能读 Issue

```text
目标仓库：<owner/repo>。下面是经我批准的完整任务（或读取 docs/tasks/<文件>.md）：
<粘贴 TASK_TEMPLATE 的完整内容，含范围、验收、批准证据；若来自不可读 Issue，保留其链接并注明内容由用户提供>
先读取仓库现状、AGENTS.md 和 PROJECT_CONTEXT.md，确认任务与实际权限。没有完整任务或批准证据时先澄清。
从最新基线创建功能分支，先把完整任务和批准记录保存到 docs/tasks/<任务名>.md，再实施、运行适用测试并如实记录。
遵守 A 指令相同的范围、安全与提交要求：任务 IN_PROGRESS → REVIEW，代码和任务一起保存在 GitHub，提交 PR 和 docs/handoff/<任务名>.md，含实际验证 ref、命令/结果、限制和下一步。
PR 创建后补回交接链接；不能推送/创建时说明阻塞，不声称完成远端交付。不得合并、发布、部署、公开或修改其他项目；等待用户返回 ChatGPT 审核。
```

可复用 [任务](templates/TASK_TEMPLATE.md) 与 [交接](templates/HANDOFF_TEMPLATE.md)。
