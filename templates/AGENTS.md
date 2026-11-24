# Project agent instructions

先读取本仓库 PROJECT_CONTEXT.md、已有规则、当前任务和最新交接，报告实际读取的 ref。保留已有程序与规范；本文件应合并接入，不覆盖已有 AGENTS.md。

只在批准范围和此项目功能分支工作。任务 PLANNED 等用户批准后才执行；记录 APPROVED、IN_PROGRESS、REVIEW，返工为 CHANGES_REQUESTED，用户接受才 ACCEPTED。

Issue 不可读时要求完整正文或 docs/tasks/ 文件。先保存完整任务及批准证据到 docs/tasks/ 再实施。实际运行适用检查，未运行如实报告。任务与代码一起留在 GitHub。

提交 PR 和 docs/handoff/ 记录：来源、基线、分支、验证 ref、文件、命令结果、限制与下一步。用户主动返回 ChatGPT 审核；审核不等于合并许可。不能推送/创建 PR 则报告阻塞，不伪造链接。

不要自行合并、部署、发布、删数据、公开仓库或修改其他项目。不要提交秘密，不声称聊天自动同步或自动唤醒。许可由所有者决定。

可选 Skill：只有初始化任务明确要求时，按框架 docs/cloud-skills.md 固定清单完整复制 .agents/skills（含第三方许可），保留本文件与原有规则。显式请求使用caveman/ponytail并确认宿主发现；不承诺云端自动继承/激活。简短或最小改动不能削弱测试、安全、批准与交接要求。
