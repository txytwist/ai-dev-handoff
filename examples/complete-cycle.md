# 完整一轮：手机上的阅读清单

这是合成演示，下面 `example-owner/reading-list`、Issue #7、PR #8 和 ref 名均是假设，不是实际创建或测试证据。真实任务应替换为可访问链接和完整 SHA；本示例不提供伪造的 GitHub URL。

## 先选入口

**新项目**：用户在 ChatGPT 粘贴初始化，说“我要一个阅读清单”。ChatGPT 核实权限；假设无建仓能力，就指导用户手机打开 GitHub 创建 Private `reading-list`，不让 Codex 重试建仓。用户授权最小初始化后，在功能分支添加 AGENTS.md、PROJECT_CONTEXT.md 和 docs/handoff/README.md，提交接入 PR 等待审核。用户另行决定合并后，继续下面的小任务。

**已有项目**：用户已有阅读清单仓库。ChatGPT 读取 README、目录、AGENTS.md，发现已有规则，提出仅补充交接条款与索引的计划。用户批准后以接入 PR 合并必要条款，不覆盖原 AGENTS.md 或程序。接入审核与合并由用户决定。然后同样进入下面一轮。

## 1. 想法与规划

用户：“请在使用说明加一句如何添加书名。”ChatGPT先读取实际项目规范，提出文档小任务，不扩展为应用。任务草案：

```text
Status: PLANNED
Repository and refs: example-owner/reading-list; base main@<真实 SHA>
Source and approval: 当前对话计划，尚未批准
Goal and scope: 在 README 的使用部分补一句添加书名的方法；只改文档
Acceptance criteria: 新手能找到说明；Markdown 相对链接检查通过；无程序修改
Plan and risks: 确认当前程序实际支持的方法，不臆造功能
Evidence: 尚未运行检查
Next action: 等用户批准
```

用户：“同意只改说明并提交 PR，不要合并。”ChatGPT把状态改 APPROVED，保存这段批准证据。假设有写权限，在项目仓库创建 Issue #7，包含上述完整任务与批准记录。

## 2. 交给 Cloud Codex

用户打开 Cloud Codex，确认仓库为自己的阅读清单，粘贴指定 Issue 的执行提示。Codex回报实际读到的标题、任务和规范，再从最新 main 创建 `docs/add-book-guide`。先保存 `docs/tasks/add-book-guide.md`，状态 IN_PROGRESS，实施与验证。

如果 ChatGPT不能写 Issue：不创建假 Issue，给用户完整任务；Codex先存同一任务文件。若 Codex读不到 Issue #7，用户提供全文并保留来源说明，再确认内容后实施。

## 3. PR 与 Handoff

演示中的 Codex交付 PR #8，任务状态 REVIEW，并保存：

```text
Status: REVIEW
Repository and refs: example-owner/reading-list; base <SHA>; docs/add-book-guide; tested <SHA>
Source and approval: Issue #7（或 docs/tasks/add-book-guide.md）；用户批准仅改说明
Changes: README 使用段新增说明；保存任务与交接
Acceptance criteria: 按实际文件与检查结果逐条填入
Evidence: <实际命令、退出码和输出摘要；没有运行则写未运行>
PR and paths: <真实 PR 链接>；docs/tasks/add-book-guide.md；docs/handoff/add-book-guide.md
Limitations: 手机阅读体验未实测；未合并或部署
Next action: 用户把 PR 与本记录带回 ChatGPT
```

此处没有声称任何命令已通过。真实交付必须提供真实测试结果。

## 4. 用户主动返回审核

用户粘贴 ChatGPT 审核提示，附 PR、提交与 Handoff。ChatGPT读取实际 diff 和证据，发现新增说明与程序支持的方法不一致，记录：

```text
Status: CHANGES_REQUESTED
Repository and refs: <实际仓库、PR head SHA>
Source and approval: 原任务及批准范围
Reviewed material: README diff、现有功能文件、测试输出
Acceptance criteria: 新手说明准确性不符合；链接检查结果另行核实
Evidence: <具体文件位置、说明与实现差异>
Decision: 建议修正文案；尚未接受
Next action: 请用户确认返工范围，更新原任务关联审核记录
```

用户批准修正文案后，Codex在原功能分支返工，任务回 IN_PROGRESS，重跑适用检查，补新 ref 的 Handoff，回 REVIEW。用户再次主动通知 ChatGPT。若 ChatGPT不能读取 GitHub，用户提供完整 diff、文件和日志，它明确只审该快照，远端状态未核实。

## 5. 接受与下一轮

ChatGPT依据证据给出可接受建议。用户明确说“接受本轮结果，暂不合并”，审核记录才变 ACCEPTED；PR仍未合并。审核记录保存 `docs/reviews/add-book-guide.md`，关联任务和交接。有写权限的 ChatGPT在授权下保存；不能写时由用户交 Codex归档。

用户另提“加书籍分类”，这是新需求，回到 PLANNED，另写任务、重新批准。合并、部署、发布或公开仓库始终需要单独决定。
