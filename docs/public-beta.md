# Public Beta：当前状态与使用

**公开测试中，许可证未确定，实机验收未完成。** 2026-11-20 开发读取 GitHub元数据确认本框架已 Public。本次任务未修改可见性；此事实不代表已验证真实 iPhone体验，也不授予开源许可。

## 手机第一次使用

1. 打开公开首页 https://github.com/txytwist/ai-dev-handoff ，选择中文或英文。
2. 点击“复制完整引导”，把唯一文本块复制到 ChatGPT 或 Gemini；无需 Fork 或向所有者取公开材料。AI读不到链接时直接粘贴全文。
3. 按规划端一次一个问题开始。你自己的项目仍可保持 Private；其读写能力需单独核实，不因框架公开而自动获得权限。
4. 外部评审可复制 [评审提示](external-ai-test.md)，用户检查脱敏结果后在 Issues提交反馈。提交反馈需登录；阅读不需。

## 仍待完成的验收

真实 iPhone上检查首页、复制、图文与 GitHub App/移动浏览器差异，见 [视觉检查单](mobile-acceptance.md)。模拟、CI和 Public 状态不能代替这些步骤。暂未完成的状态仍是 NOT_RUN，不假称已成功。

隐私持续复核包括 Git文件/历史/身份元数据，以及 Issue、PR、评论、附件、Actions日志/artifacts；启发式脚本不是全平台安全认证。历史 tasks/Handoff保留当时状态，是历史快照，不是当前入口。许可继续保留 LICENSE_PENDING，不修改或补 MIT。

合并、部署、发布、改可见性和选择许可仍须用户分别决定；本文不再要求已公开仓库重新切换 Public，也不会替用户操作设置。
