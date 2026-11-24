# PR #15 默认继承修订 Handoff

## Status
REVIEW；沿用原分支和PR，不合并。

## Repository and refs
txytwist/ai-dev-handoff；原分支feat/cloud-skill-compatibility；修订基线e21bfd3。最终head见PR。

## Source and approval
[本轮任务与用户批准](../tasks/cloud-skills-defaults.md)。先前可选兼容性实验记录是历史快照，本轮需求已替换为默认继承。

## Changes
新项目初始化器默认创建AGENTS、上下文、交接索引与完整固定Skill包；只有显式--disable-skills才不复制，并在上下文保存用户禁用决定。允许初始README，其他已有文件拒绝覆盖。模板与根AGENTS要求每次新会话主动读完整Skill并执行，仅用户明确禁用时跳过，失败报告；所有初始化提示同步，原安全/测试/授权/交接条款保留。固定上游正文、manifest与许可证未改。

## Acceptance criteria
自动测试覆盖默认初始化、禁用记录、基础文件及新会话规则、重复初始化拒绝、原规范保留、损坏Skill拒绝；真实原生发现再次检查。不把模板要求/文件存在当作自动激活已通过。

## Evidence
2026-11-24实际运行，退出码均为0：

```text
python3 scripts/verify_repo_skills.py --host
PASS: default new-project skills, full hashes, per-session policy, explicit opt-out record, no-overwrite, preserved guidance, corruption rejection.
codex-cli 0.167.0-alpha.4
PASS: native skills/list discovers enabled repo skills without parse errors in source and fresh project; discovered paths readable.
python3 scripts/validate.py
PASS: 41 required files; 45 Markdown files; 97 local links; shared template fields; states; 46 files scanned for common sensitive patterns.
python3 scripts/test_validate.py
PASS: clean fixture accepted; missing file/workflow, broken link, missing field and synthetic token and stale private onboarding rejected; temporary fixture removed.
PASS: privacy scanner detects synthetic token/email; flags non-UTF8 as unscanned; accepts ordinary text.
git diff --check
无输出，通过。
```

新增默认初始化与显式禁用测试复用现有CI检查入口；真实网页新会话模型执行/自动激活仍NOT_RUN。最新远端CI结果以PR对应head为准。

## 验证分级

- 原生发现：本仓库与默认初始化的新项目中，codex app-server skills/list均发现两个enabled repo Skill，无解析错误。
- 正文读取：本轮助手用工具完整读取两份SKILL.md；程序核对原生返回路径及SHA256。
- 实际执行：本轮助手按文件指令采用简短但保留载荷的交流、复用标准库、最小完整修订、运行必要测试及保留完整交接。这是当前会话文件指令执行，不是新的独立模型原生路由证据。
- 新会话自动激活：NOT_RUN；AGENTS的主动加载要求已经配置，但未在真实Cloud Codex网页新任务中观察，不声明产品能力已实测。
- 用户禁用：程序测试显式禁用不复制且记录；按自然语言只禁用某一个Skill的实际新会话响应仍未验证。

## PR and paths
https://github.com/txytwist/ai-dev-handoff/pull/15 ，最新说明见 [默认继承](../cloud-skills.md)。

## Limitations
原生发现与本轮文件指令执行不等于新网页会话自动激活或跨会话模式持久化。初始化器只接受新项目，已有项目需按授权计划合并，不覆盖规范；加载失败必须报告而非降级伪称通过。未测试手机或新增上游hooks/代理/全局配置。未改main、许可或可见性。

## Next action
ChatGPT审核本PR最新diff和结果；新会话原生执行/自动激活的产品面验证仍待独立实际观察。不自行合并。
