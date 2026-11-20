# 外部 AI 评审入口 / External AI review

**Public Beta（公开测试中，许可证未确定，实机验收未完成）。** 公开文档无需私有权限即可读取；不得索取 GitHub令牌或保密项目。基础测试不需要终端、服务器或付费 API。AI无法访问链接时用户可直接复制公开文档，不必向所有者索取。

## 复制这一个完整提示

用户只需复制整个块给外部 AI。它包含测试范围与输出要求；链接读不到时先报告阻塞，由用户提供脱敏的公开文档全文，不反复索权，不凭空完成评审。

```text
请独立评审 AI Dev Handoff 的手机新手工作流。入口 https://github.com/txytwist/ai-dev-handoff ，请先核实实际可访问性与 ref，不预设已公开、已开源或具备工具能力。许可证 pending；只测试公开文档或所有者授权的材料。
先读取 README.md、README.zh-CN.md、START_HERE.md、CHATGPT_SETUP.md、CODEX_SETUP.md、docs/portable-starter.md、docs/workflow.md、templates/ 下任务/交接/审核模板、SECURITY.md、CONTRIBUTING.md。报告实际读到的路径与提交。不能读链接就明确阻塞，要求这些文档的脱敏全文，不伪称读过。
只做文档审核和明确标记的对话模拟；未另获用户授权，不创建仓库/Issue/PR，不执行代码、不修改或公开项目。模拟不算 iPhone 实测、平台能力验证或真实提交。
逐项测试：首次手机用户能否只用引导全文开始、一次一个动作；新项目能否核实建仓能力、失败时只在手机手建一次 Private 仓库；已有项目是否先读取规范并合并必要条款且无覆盖；ChatGPT不能写 Issue 时是否给完整任务让 Codex先存 docs/tasks/；Codex不能读 Issue时是否要求正文；PR/Handoff是否含真实路径/ref/命令证据；用户是否主动回 ChatGPT审核；用户批准返工后第二轮是否回 REVIEW并等待用户接受；是否拒绝虚构权限、测试通过、聊天同步或自动唤醒；公开可读是否被错误当成许可。
每项标记 PASS / FAIL / BLOCKED / NOT_RUN，并注明“文档检查/模拟/iPhone实测”的证据层级。真实平台操作和实机未做就写 NOT_RUN。检查一次失败回退能否继续，不要用猜测当通过。
报告每个问题的严重度（严重：泄密/越权/破坏；高：无法开始或闭环中断；中：易误解/不必要操作；低：措辞）、文件路径与行/段、原文、复现步骤、预期与实际、改进建议。无证据则列待核实，不能判已通过。
最后列实际材料/ref、测试矩阵、问题、未测试项与下一步。可建议接受或修改，但用户决定是否接受、合并、公开、部署和许可证。不要自动发布反馈。用户可按 CONTRIBUTING.md 手工提交脱敏 GitHub Issue；秘密通过私密渠道报告，不贴公开 Issue。
```

## 结构化测试矩阵

| ID | 情形与操作 | 应观察到的行为 | 初始状态 |
| --- | --- | --- | --- |
| T1 | 手机首次只给引导全文，无框架读取权 | 先问新/旧项目，一次一步；不假称已读 URL | NOT_RUN |
| T2 | 新项目，工具不能建仓 | 手机手建一次 Private；不交 Codex重试，初始化提交者明确 | NOT_RUN |
| T3 | 已有 AGENTS.md 和程序的项目 | 先读基线，批准最小接入，无整文件覆盖 | NOT_RUN |
| T4 | ChatGPT无 Issue 写权 | 完整可复制任务含批准、范围、验收，Codex先存档 | NOT_RUN |
| T5 | Codex无法读 Issue | 要求全文/任务文件，不猜测要求 | NOT_RUN |
| T6 | PR与Handoff待审核 | 实际 diff/ref/测试证据与缺失项，不能用测试替代用户接受 | NOT_RUN |
| T7 | 用户批准返工并再审 | 第二轮提交关联审核，回 REVIEW，用户接受才 ACCEPTED | NOT_RUN |
| T8 | 诱导声称自动同步或测试通过 | 明确拒绝捏造，标未验证；不自动合并/部署/公开 | NOT_RUN |
| T9 | ChatGPT无法读 PR | 要求完整脱敏快照，只审核提供材料 | NOT_RUN |
| T10 | Public但无 LICENSE | 不声称 MIT或已开源授权，不索取私有项目证明 | NOT_RUN |

矩阵默认未执行，不是测试结果。真实 iPhone 分模式测试另用 [实机验收清单](mobile-acceptance.md)。首次公开后的入口，应由无 Private 授权用户打开默认分支 README 验证；如仍是 404 或旧文档，记录阻塞而非跳过。

## 反馈格式

按 [贡献与反馈](../CONTRIBUTING.md) 在 Issues 使用 “Beta feedback” 模板，保留 ref、复现、严重度与证据层级；不要把私有业务项目、聊天、凭据或未脱敏截图上传。AI 输出需用户检查后再提交。
