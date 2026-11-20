# Public Beta 准备任务

## Status
REVIEW

## Repository and refs
`txytwist/ai-dev-handoff`，基线 `main@d036991`，分支 `feat/public-beta-readiness`。

## Source and approval
https://github.com/txytwist/ai-dev-handoff/issues/3 （正文已读取，无评论）。用户 2026-11-20 明确要求准备、测试、PR 与交接，不授权合并、改可见性或添加许可。

## Goal and scope
过渡期真实文案、外部 AI 自包含评审提示和测试矩阵、安全/隐私检查、反馈路径、所有者手机公开步骤。仅此仓库；不涉及其他项目。

## Acceptance criteria
入口兼容 Private 和未来 Public Beta；一块可复制外部审核提示；结构化场景；跟踪文件及可获取历史的隐私检查与限制；现有校验和 CI；PR/Handoff。

## Plan and risks
先核实基线与状态，补文档及可复现隐私审计，运行静态检查；发现历史元数据不能擅自改写。仍需所有者评估隐私与用户实测。

## Evidence
见 [Handoff](../handoff/public-beta.md)。

## Next action
PR https://github.com/txytwist/ai-dev-handoff/pull/4 ，状态 REVIEW，等待 ChatGPT 审核。许可、合并与 Public 都单独决定。
