# 工作流与审核闭环

## 分工

用户决定目标、授权与接受结果。ChatGPT 规划、优先写 Issue、审查实际改动。Cloud Codex 在用户选择的仓库实施、测试、提交 PR 和 Handoff。三方没有自动聊天共享或唤醒机制。

## 状态与证据

| 状态 | 谁推动、需要什么 |
| --- | --- |
| PLANNED | ChatGPT 提出任务草案、范围与验收条件 |
| APPROVED | 用户明确同意范围；任务记录批准原文或可追溯消息摘要 |
| IN_PROGRESS | 用户启动 Codex；已读取任务和项目规范，已保存任务 |
| REVIEW | Codex 提交变更和证据、PR、Handoff，等待用户通知 ChatGPT |
| CHANGES_REQUESTED | 审核指出具体问题；用户确认返工范围后再交 Codex |
| ACCEPTED | 用户明确接受结果，保留审核与决定记录 |

正常流转：PLANNED → APPROVED → IN_PROGRESS → REVIEW → 用户决定 ACCEPTED 或 CHANGES_REQUESTED。返工批准后回 IN_PROGRESS。新需求回 PLANNED。任务文件是状态记录；Issue/PR 开关状态不等于业务验收。

## 任务持久化

有权限时 ChatGPT 在用户项目仓库创建 Issue。Codex 保存批准范围和来源到 `docs/tasks/`，避免聊天丢失。ChatGPT 无写权限则用户粘贴完整任务；Codex 无 Issue 读取权限则提供版本化任务或正文。任务未读全不实施。每次保留来源、仓库、基线、批准、验收。

## 审核实际变更

用户返回 ChatGPT 提供 PR、提交 SHA 与 Handoff。ChatGPT核对批准范围与实际 diff，逐条评估验收，查测试命令与输出，指出未解决风险。没有 GitHub 读权限时要求完整 diff、文件、测试日志和 ref，并明确只审核所提供快照，远端状态未核实。

用 [审核模板](../templates/REVIEW_TEMPLATE.md) 保存结果到项目 `docs/reviews/`；有写能力的 ChatGPT 在授权范围内保存，否则用户把记录交 Codex归档。返工创建/更新任务，关联原 PR 和审核。每轮 Handoff 记录验证过的提交；后续代码变动使旧证据不自动覆盖新提交。

用户接受后是否合并、部署、发布、公开仓库分别决定。本流程不自动执行这些动作。不能用“测试通过”代替生产验证。
