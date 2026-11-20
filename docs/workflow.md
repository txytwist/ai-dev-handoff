# 工作流与审核闭环

## 分工

用户决定目标、授权与接受结果。ChatGPT 规划、优先写 Issue、审查实际改动。Cloud Codex 在用户选择的仓库实施、测试、提交 PR 和 Handoff。三方没有自动聊天共享或唤醒机制。

## 两种流程对比 / Workflow comparison

这是**无统一交接机制的典型手动示例**与**有真实权限、经用户授权的 AI Dev Handoff** 的说明性对比，不是对其他工具的必然断言，也没有实测性能数据。两图纵向排列，节点短句分行；手机可逐图阅读。图中只用中文短标签；每图下方保留完整中英文文字版。

These are illustrative scenarios, not universal claims or measured outcomes. Short Chinese labels run top to bottom; full equivalent Chinese and English text follows each diagram.

### 无统一交接 / Without structured handoff

```mermaid
flowchart TD
  A["用户提想法"] --> B["ChatGPT讨论"]
  B --> C["用户传上下文"]
  C --> D["Codex实现"]
  D --> E["用户整理结果"]
  E --> F{"证据完整？"}
  F -->|否| C
  F -->|是| G["用户决定下一步"]
```

文字版：用户提想法 → ChatGPT讨论 → 用户传递上下文 → Codex实现 → 用户整理结果；证据不全则补上下文，证据齐全后用户判断下一步。其他手动流程也可能保留完整记录。

Text: idea → discussion → user copies context → implementation → user gathers results; fill gaps if evidence is incomplete, otherwise the user decides next. Other manual workflows may also keep complete records.

### 统一交接 / With AI Dev Handoff

```mermaid
flowchart TD
  A["用户提目标"] --> B["规划与验收"]
  B --> C{"用户批准？"}
  C -->|修改| B
  C -->|批准| D["GitHub任务"]
  D --> E["用户启动Codex"]
  E --> F["开发与测试"]
  F --> G["PR与交接"]
  G --> H["用户返回ChatGPT"]
  H --> I["证据审核"]
  I --> J{"用户决定"}
  J -->|返工| B
  J -->|接受| K["记录接受"]
  K --> L["合并另授权"]
  L -->|新任务| B
```

文字版：目标 → 规划 → 用户批准 → 持久任务 → 用户启动 Codex → 实施测试 → PR/交接 → 用户返回 ChatGPT → 证据审核 → 用户决定；返工先批准修改范围，新任务重新规划。接受不自动合并。

Text: goal → plan → user approval → durable task → user starts Codex → implementation/tests → PR/handoff → user returns to ChatGPT → evidence review → user decision. Rework needs approved scope; new tasks return to planning. Acceptance does not merge a PR.

**没有统一交接机制时，用户常要兼任传话者与上下文整理者；有 AI Dev Handoff 后，用户仍掌握决策权，但规划、执行、记录和审核有了明确分工。**

**Without a structured handoff, the user often acts as messenger and context keeper. With AI Dev Handoff, the user remains in control while planning, execution, records and review have clear owners.**

权限与边界：ChatGPT仅在有实际权限及授权时优先写 Issue；写不了则给完整任务。Codex必须确认 Issue可读，读不到用正文或版本化 `docs/tasks/`，先保存批准任务再执行。图中的 GitHub记录属于**用户自己的项目仓库**。每次切换由用户主动发起，没有聊天自动同步或自动唤醒。审核、用户接受、合并/部署/公开授权是不同决定；图中没有自动合并。

Permissions and boundaries: ChatGPT prefers Issues only with actual write access and authorization; otherwise it supplies a full task. Codex verifies Issue access and falls back to pasted content or versioned `docs/tasks/`, saving the approved task before implementation. Records belong in **the user's own project repository**. Users initiate every switch; chats do not auto-sync or wake each other. Review, acceptance, and permission to merge/deploy/publish are separate decisions. No automatic merge is shown.

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
