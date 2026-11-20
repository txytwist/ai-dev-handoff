# 贡献与维护

先在 Issue 说明范围和验收，再经用户批准在功能分支提交。文档优先，不引入服务端应用或运行时依赖。只提交通用示例，不带私有项目材料。

维护者在 Cloud Codex 环境运行：

```sh
python3 scripts/validate.py
python3 scripts/test_validate.py
git diff --check
```

Python 3 标准库即可，无需联网或安装包。普通手机用户不需运行；让 Codex 在 PR/Handoff 提供真实输出。校验覆盖必需文件、文档相对链接、共享模板字段及常见凭据特征；不验证外部链接、平台权限、手机 UI 或穷尽秘密。人工仍需检查可读性与闭环。

PR 使用 [PR 模板](.github/pull_request_template.md)，交付 REVIEW 并等待用户审核，不自行合并或发布。新项目规则使用 [可复用 AGENTS](templates/AGENTS.md)。许可证待决定，贡献接收及未来许可须由所有者确认。

## 验证分级与远端结果

本地命令通过仅证明当前静态快照。`.github/workflows/docs.yml` 在 push/PR 事件运行相同标准库检查及故障用例，结果看 PR Checks 中的 `documentation` 或仓库 Actions，核对运行对应 head SHA。无 CI 记录、被账户策略禁用或失败都不写成通过；状态以实际 run 为准。只用只读 contents 权限，不读取秘密、不安装 Python 包、不部署。GitHub runner 与 checkout 仍需 GitHub 托管环境可用。

CI不等于真实 iPhone 端到端验收；两种模式、权限回退与第二轮记录见 [待办清单](docs/mobile-acceptance.md)。当前均未实测。

## Public Beta 反馈

外部 AI 提示与矩阵见 [评审入口](docs/external-ai-test.md)。Public 后可在仓库 Issues 新建 “Beta feedback” 报告；Private 阶段只有授权成员可用，其他测试者把脱敏报告交所有者，由其决定记录。不能承诺工具能自动发 Issue。

手机无需 CLI：打开仓库 Issues 创建反馈，选模板；无模板时复制其正文。填写提交 ref、文件路径/行段、严重度、复现步骤、预期/实际、证据及未测试项，区分文档/模拟/实机。AI起草后由用户检查再提交。公开反馈绝不能带密码、令牌、个人数据、私有业务仓库材料或未脱敏聊天/截图。敏感问题走 SECURITY.md 私密流程，不为证明漏洞而公开秘密。

Public 可读不代表获得开源许可证。许可未定时不要承诺他人可任意复制、再分发或商用；授权问题由所有者决定。

公开准备审计（维护者在 Codex执行，不要求手机用户运行）：`python3 scripts/privacy_audit.py`。需完整授权获取的历史；报告计数、范围、命中类型及元数据暴露风险，不把未扫描对象当成安全。
