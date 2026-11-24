# 云端 Skill 兼容性 Handoff

## Status
REVIEW；只交付兼容性实验，无自动合并。

## Repository and refs
`txytwist/ai-dev-handoff`；基线main@9c0ecb7；分支feat/cloud-skill-compatibility。NEXT_TASK.md不存在。最终head见PR。

## Source and approval
[任务](../tasks/cloud-skills.md)，用户2026-11-24明确授权。已读AGENTS、初始化及Codex执行规范。

## Changes
固定官方上游完整核心Skill目录、保留许可与NOTICE、SHA256清单；两个repo级Skill；可选初始化复制与校验脚本；原生skills/list检测；初始化/规则补充与CI完整性检查。根项目许可证不变，第三方许可仅作用于导入文件。

## Acceptance criteria
来源、文件、许可、原生发现、实际读取与显式复制继承有证据。执行样例分级记录，不声称新的网页云端会话已原生路由或自动激活。现有开发/测试/安全/交接规范继续适用。

## Evidence
2026-11-24 实际运行，退出码全部为0：

```text
python3 scripts/verify_repo_skills.py --host
PASS: complete pinned files, hashes, fresh-project inheritance, no-overwrite guard, preserved AGENTS, corruption rejection.
codex-cli 0.167.0-alpha.4
PASS: native skills/list discovers enabled repo skills without parse errors in source and fresh project; discovered paths readable.
python3 scripts/validate.py
PASS: 41 required files; 43 Markdown files; 92 local links; shared template fields; states; 44 files scanned for common sensitive patterns.
python3 scripts/test_validate.py
PASS: clean fixture accepted; missing file/workflow, broken link, missing field and synthetic token and stale private onboarding rejected; temporary fixture removed.
PASS: privacy scanner detects synthetic token/email; flags non-UTF8 as unscanned; accepts ordinary text.
git diff --check
无输出，通过。
```

同一CLI原生RPC在添加Skill前不包含caveman/ponytail；添加后与新项目测试目录均返回两个repo Skill、enabled=true、各自SKILL.md路径，无errors。上游完整目录和SHA256在manifest中可复核，新增CI检查仅使用标准库，不依赖Codex或模型。

远端Actions以PR对应head的真实结果为准，不把本地结果替代远端检查。

## 本轮指令执行样例（当前助手，非独立原生会话）

助手已实际读取两份SKILL正文；caveman按“短答但技术载荷和否定词完整、持久文档正常语言”执行。受控输入：用中文保留命令、未实测与禁止合并，简短报告。输出：

> 已验证仓库发现与继承：`python3 scripts/verify_repo_skills.py --host`。手机实测未运行。不得合并。

ponytail按“最小完整改动、复用标准库、不能省验证/安全”执行。受控输入：给保留AGENTS的新项目继承最小方案。输出：

> 复用 `scripts/init_repo_skills.py` 复制完整技能与许可，已有技能拒绝覆盖，保留AGENTS。用 `python3 scripts/verify_repo_skills.py --host` 检查。未安装上游hooks、CLI或代理；新云端网页会话自动激活未验证。

这些是本轮按文件指令实际编写的回答，不是伪造的Codex模型调用/工具日志。没有启动额外模型或自动唤醒其他会话；不把模仿短答当成原生路由证据。

## PR and paths
PR创建后补回。来源/许可/完整性边界及复现步骤见 [兼容性说明](../cloud-skills.md)。

## Limitations
原生发现与可读通过不等于所有产品界面能自动触发。当前会话新增文件不能追溯修改启动时的Skill目录；真实网页新会话调用/路由、跨会话模式、手机、上游未导入插件/命令均未验证。不削弱批准/测试/安全/完整交接，不改全局配置、main或可见性。

## Next action
ChatGPT审核PR与固定上游文件；用户如需完整产品面结论，在新云端任务选择含该分支的仓库显式调用两个Skill，再记录模型执行证据。不得自行合并。
