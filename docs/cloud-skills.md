# caveman / ponytail：默认继承与云端验证

新项目默认继承两个仓库Skill；只有用户明确禁用时才跳过并记录。基础安全、测试和授权规范不因Skill加载失败而被删除。目录 `.agents/skills/` 只配置两份指令型Skill，不装上游软件栈、代理、hooks、全局规则、遥测或额外插件；不是ChatGPT手机Skill安装承诺。

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
- 新项目继承：临时Git新项目运行默认初始化器，无需Skill选项即生成现有AGENTS/PROJECT_CONTEXT模板、交接索引及完整技能包；原生skills/list也在该cwd发现两个repo Skill，AGENTS逐字节保留。重复复制被拒绝，损坏文件校验失败。
- 未验证：真实Cloud Codex网页选择新仓库后新会话的自动发现/显式路由与跨会话模式持久化；ChatGPT iOS安装；未安装的上游hooks/插件、其他别名。不要把app-server发现当成全部产品表面的执行证明。

## 新项目默认初始化

用户批准新项目初始化后，默认生成AGENTS.md、PROJECT_CONTEXT.md、docs/handoff/README.md并完整继承 `.agents/skills/`（manifest、两份Skill与许可）。无需另行请求Skill，不Fork框架。每次新会话必须主动读取并执行两份Skill，仅用户明确禁用的Skill跳过；禁用范围/原因与加载失败必须报告。原生调用失败但文件可读时标记按文件执行；文件也不可读时暂停依赖Skill的步骤，不能伪称已执行。

框架工作区中，Codex运行（普通手机用户无需终端）：

```sh
python3 scripts/init_repo_skills.py <approved-new-project-root>
```

目标必须是已获准的新Git仓库根，允许已有初始README，但不允许其他已有项目文件；拒绝重新初始化/覆盖原规范。已有项目按接入计划人工合并，不强行运行新项目初始化器。脚本不会提交或合并，也不会改项目许可或全局配置。

只有用户明确禁用两个Skill时才运行：

```sh
python3 scripts/init_repo_skills.py <approved-new-project-root> --disable-skills
```

该标志记录用户明确禁用到PROJECT_CONTEXT.md，仍生成保留全部安全/测试/授权/交接规则的AGENTS。会话中只禁用某一个Skill时，按用户指令/项目上下文记录范围，仅跳过该Skill，不把其中一个被禁用推成全部禁用。每次会话检查最新禁用决定；未指定不是禁用。

验证命令：

```sh
python3 scripts/verify_repo_skills.py
python3 scripts/verify_repo_skills.py --host
```

第一条离线标准库检查完整性、继承、保护规则和损坏样例，可在GitHub Actions跑。第二条需本机Codex CLI，额外实际调用原生发现接口；无CLI或协议错误应报告阻塞，不当作通过。脚本不会调用模型或运行上游安装器。

## 新会话执行要求与证据边界

AGENTS模板已经要求每次新会话主动加载并执行，不需要用户再次说“使用Skill”。这是应遵守的规则，不是产品自动激活已验证的结论。新会话需回报读取路径、禁用决定、失败原因与实际执行证据；交接分别列出原生发现、读取、实际执行和自动激活。

本轮程序已验证默认初始化产物、禁用记录与原生发现；当前助手读取全文后按文件指令执行。真实Cloud Codex网页新会话自动激活、原生模型路由及跨会话持久化仍未验证，不能以AGENTS文字或app-server发现结果冒充通过。
