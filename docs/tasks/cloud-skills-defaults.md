# PR #15 默认继承修订

## Status
REVIEW

## Repository and refs
原分支feat/cloud-skill-compatibility，修订基线e21bfd3，沿用PR #15。

## Source and approval
用户2026-11-24明确要求默认继承两份Skill、每次新会话主动读取执行、仅明确禁用时跳过、失败报告、保留既有规范、更新流程与自动测试；不新开PR或合并。

## Goal and scope
将现有可选复制器改成默认包含Skill的新项目初始化器；更新模板及所有初始化入口，保留上游固定字节/许可与已有安全边界，分级记录验证。

## Acceptance criteria
默认生成三份基础文件与完整Skill包；显式禁用有记录且不删规范；拒绝覆盖；每会话模板要求及失败报告清楚；静态/原生发现测试通过，不伪造新会话自动激活。

## Evidence
见 [本轮交接](../handoff/cloud-skills-defaults.md)。

## Next action
等待ChatGPT审核 https://github.com/txytwist/ai-dev-handoff/pull/15 。
