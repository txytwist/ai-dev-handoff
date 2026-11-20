# Public Beta 准备 Handoff

## Status
REVIEW；未合并、未改可见性、未添加许可证。

## Repository and refs
`txytwist/ai-dev-handoff`；基线 `main@d036991`，分支 `feat/public-beta-readiness`。最终 SHA 在 PR 与最终回复提供，避免交接自引用。

## Source and approval
Issue https://github.com/txytwist/ai-dev-handoff/issues/3 及用户本次明确授权；任务见 [public-beta](../tasks/public-beta.md)。仅公开测试准备，不是公开授权。

## Changes
README双语与首次使用入口改成条件化 Private/Public Beta 表述，许可独立待定；新增外部 AI 自包含评审提示、T1–T10 测试矩阵、Beta反馈模板、反馈隐私规范、所有者手机开放与匿名入口验证步骤；新增可复现跟踪文件/可获取历史审计脚本。原有实机未测标记保留。

## Acceptance criteria
公开测试材料已备齐；实际公开、匿名入口和真实 iPhone测试仍未执行。所有者需先评估隐私检查限制和 Git 作者元数据，决定接受/返工与是否合并、何时 Public。

## Evidence
2026-11-20 实际本地运行，退出码均为 0：

```text
python3 scripts/validate.py
PASS: 37 required files; 32 Markdown files; 74 local links; shared template fields; states; 33 files scanned for common sensitive patterns.
python3 scripts/test_validate.py
PASS: clean fixture accepted; missing file/workflow, broken link, missing field and synthetic token rejected; temporary fixture removed.
PASS: privacy scanner detects synthetic token/email; flags non-UTF8 as unscanned; accepts ordinary text.
git diff --cached --check
无输出，通过。
```

隐私审计：先 `git fetch origin`，`git rev-parse --is-shallow-repository` 为 false；本地已获取 main 与原功能分支 refs。新增文件暂存后运行 `python3 scripts/privacy_audit.py`：37 个跟踪文件、46 个唯一可达 blob、6 个提交、0 非 UTF-8 跳过，无内容模式命中；2 组作者/提交者姓名/邮箱组合仍待所有者评估。该计数是提交前基线历史快照；交付提交后重跑的范围会增加。仅对已获取 refs 作结论，不代表全 GitHub 历史或全量平台数据安全。已排除校验器内“无关项目名”检测规则的定义行（已知扫描签名，不是借用的项目材料）。不在报告中回显潜在秘密或邮箱。

远端 CI：PR 创建后检查实际 run；未运行前不声称通过。

## PR and paths
创建后补回本分支 PR；`docs/external-ai-test.md` 为评审入口，`docs/public-beta.md` 为所有者操作，`.github/ISSUE_TEMPLATE/beta-feedback.md` 为反馈模板。

## Limitations
启发式扫描不穷尽秘密。只覆盖本地可获取 refs，未获取/已删远端对象不在范围；GitHub Issues/PR/评论/附件/Actions日志/artifacts未完成全量隐私复核。Git元数据可能暴露作者姓名和邮箱，不能将内容扫描无命中当作所有者已接受。没有重写历史、修改其他项目或读取真实业务凭据。iPhone与外部 AI实测未运行；许可证待定不等于开源授权。

## Next action
ChatGPT审查实际 diff、检查及上述未知风险；所有者决定是否接受、合并，并在合并后另行决定公开。若决定 Public，按手机步骤操作并用无私有授权会话验证入口；不由 Codex执行。
