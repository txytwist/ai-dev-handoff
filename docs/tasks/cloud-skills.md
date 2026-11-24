# 云端 Skill 兼容性验证

## Status
REVIEW

## Repository and refs
`txytwist/ai-dev-handoff`；基线 `main@9c0ecb7`；分支 `feat/cloud-skill-compatibility`。NEXT_TASK.md 不存在。

## Source and approval
用户 2026-11-24 明确批准：核查 caveman/ponytail 来源、许可、完整文件；配置仓库 Skill；验证云端发现/读取/执行和新项目继承；保留现有规范，PR后不合并。已读 AGENTS.md、CODEX_SETUP.md、START_HERE.md、templates/AGENTS.md。

## Goal and scope
仅指令型 Skill 的兼容性实验，不安装上游 CLI、代理、hooks、遥测、插件或全局配置；不改 main、仓库可见性或根许可证。

## Acceptance criteria
固定官方仓库提交、保留完整Skill目录及许可、SHA256清单；原生skills/list的repo发现证据；读取及指令试运行如实分级；新项目初始化显式复制验证；未验证项不伪造通过。

## Evidence
见 [交接](../handoff/cloud-skills.md)。

## Next action
完成后 REVIEW，等待ChatGPT审核。
