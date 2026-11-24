# caveman / ponytail：仓库级云端兼容性实验

基础工作流不依赖本实验。目录 `.agents/skills/` 只配置两份指令型Skill，不装上游软件栈、代理、hooks、全局规则、遥测或额外插件；不是ChatGPT手机Skill安装承诺。

## 官方来源与许可

2026-11-24 核查上游README的自认来源、安装指引及许可文件（不是独立身份认证或安全认证）：

- caveman：https://github.com/JuliusBrussee/caveman ，固定提交 `47c61be2d10a354f0c5cbe2b90959d24c06b16c6`。README自链本仓库并提供其skills安装命令；LICENSING.md明确3.0.0起含Skill为Apache-2.0。保留根LICENSE、NOTICE及NOTICE引用的LICENSE-MIT。商标不随代码许可授权，无上游背书声明。
- ponytail：https://github.com/DietrichGebert/ponytail ，固定提交 `ebd8654c2c627f721eb8f9c0d1bd4090a29f9e10`。README明确只从该GitHub仓库或其npm作者名安装，且说明核心提示位于skills/ponytail/SKILL.md。其LICENSE为MIT，Copyright (c) 2026 DietrichGebert，随副本保留。

这些第三方许可仅适用于标明的第三方文件；不为AI Dev Handoff根项目选定许可证，LICENSE_PENDING.md不变。

完整性边界：复制固定提交中 `skills/caveman/` 的两个文件（SKILL.md、README.md），`skills/ponytail/` 的唯一文件SKILL.md，以及上述许可声明。两份SKILL.md逐字节保留。caveman README只新增包装变更说明、把三个移位后的相对链接改成固定提交URL。所有上游路径、原始与安装后SHA256见 `.agents/skills/manifest.json`。未导入上游其他Skill或完整CLI/插件仓库；`ultracave`、`megacave`、附加命令、hooks状态持久化均不在本包范围。

## 当前环境验证分级

- 本次Codex云端机器中的CLI版本：`0.167.0-alpha.4`。
- 原生协议：`codex app-server` initialize 后 `skills/list`，参数包含当前仓库cwd与forceReload=true，两个名字均返回enabled=true、scope=repo、各自仓库内SKILL.md路径，errors为空。
- 实际读取：校验程序读取原生返回路径并核对前言；本轮助手已读取完整Skill正文，再按指令完成下方受控试运行。
- 指令执行样例：当前助手直接应用文件指令，**不是新增模型会话的原生 `$skill` 路由日志**。不能拿这个样例证明网页自动激活。样例见Handoff。
- 新项目继承：在临时Git新项目放入现有AGENTS/PROJECT_CONTEXT模板与交接索引，显式复制完整技能包；原生skills/list也在该cwd发现两个repo Skill，AGENTS逐字节保留。重复复制被拒绝，损坏文件校验失败。
- 未验证：真实Cloud Codex网页选择新仓库后新会话的自动发现/显式路由与跨会话模式持久化；ChatGPT iOS安装；未安装的上游hooks/插件、其他别名。不要把app-server发现当成全部产品表面的执行证明。

## 新项目初始化的显式继承

初始化仍按START_HERE批准范围、最小规范/上下文/交接索引、功能分支与PR，不自动Fork或继承技能。若用户要求此实验，在已获准目标仓库根目录添加完整 `.agents/skills/`（manifest、两份Skill目录和各自许可不能遗漏），**不覆盖已有AGENTS或其他Skill**。

在框架工作区，维护者可运行：

```sh
python3 scripts/init_repo_skills.py <approved-project-root>
```

它只复制技能，不代替整个项目初始化，不提交/合并、不修改项目规范。目标必须是Git根目录，已有skills或符号链接则拒绝；已有项目应人工评审合并方案，不能强行覆盖。手机用户把该步骤放入批准任务交Codex执行，无需手机终端。

验证命令：

```sh
python3 scripts/verify_repo_skills.py
python3 scripts/verify_repo_skills.py --host
```

第一条离线标准库检查完整性、继承、保护规则和损坏样例，可在GitHub Actions跑。第二条需本机Codex CLI，额外实际调用原生发现接口；无CLI或协议错误应报告阻塞，不当作通过。脚本不会调用模型或运行上游安装器。

在新云端会话主动请求：“读取AGENTS.md，核实两个仓库Skill的实际路径；本轮按 `$caveman` 和 `$ponytail` 执行批准任务，保留测试、安全与完整交接要求。不能发现或调用就明确报告。”需要用户在新项目、新会话实际完成这一剩余产品面验收，不能由本轮测试目录结果代替。
