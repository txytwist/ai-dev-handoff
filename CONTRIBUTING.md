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
