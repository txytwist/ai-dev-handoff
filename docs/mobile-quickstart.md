# 每天在手机上操作

第一次使用请走 [一页逐步路线](../START_HERE.md)；AI无法读链接时，直接复制公开的 [完整引导全文](portable-starter.md) 给它。当前为 Public Beta，许可证待定，实机验收未完成。

1. **ChatGPT / Gemini 提想法**：打开项目对话，说“请读取项目规范，我想做……，先给最小方案和验收标准”。看懂后明确批准。让规划端优先创建项目 Issue；不能写则复制完整任务。
2. **Codex / Antigravity 执行**：打开 Cloud Codex 或 Antigravity，选择正确项目，粘贴 [执行指令](../CODEX_SETUP.md)。先确认它读到了正确任务并核验了 `NEXT_TASK.md` 是否滞后；读不到就提供全文。等待PR链接（含详细交接）。
3. **ChatGPT / Gemini 审核**：主动返回，粘贴 [审核请求](../CHATGPT_SETUP.md) 并附PR链接，由其读取提交与交接。查看问题与证据，明确说“接受”或“按这些问题修改”。新需求重新规划。

不要在不理解时批准。PR 是变更提案，未合并前默认分支通常不会包含新功能。接受结果不自动合并；需要时再单独决定。首次使用看 [初始化](../START_HERE.md)，完整演示看 [示例](../examples/complete-cycle.md)。
