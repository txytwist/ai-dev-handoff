# 项目开发与交接规范

## 沟通与分工

默认简体中文，结论优先，只保留必要信息；手机操作优先，每次只给一个必要的手动步骤，优先用已可访问的GitHub链接，尽量减少复制。术语首次出现时简短解释：Issue是任务单，PR是待审核的变更提案，Skill是供AI读取执行的指令包。交付尽量只给一个PR链接，有阻塞补充一句说明；完整证据放在PR。

GitHub是项目记录的准绳。规划/审核端（ChatGPT 或 Gemini）负责规划、权限及授权允许时建仓和创建Issue、审核PR；执行端（Cloud Codex 或 Antigravity）负责独立功能分支开发、测试及交付。用户主动发起交接，不假设聊天自动同步或自动唤醒。无权限时报告限制，不伪称已读、已写或已审核。

## 接手与实施

每次接手先读取 AGENTS.md、NEXT_TASK.md（如存在）、当前 Issue/PR及评论，再读取PROJECT_CONTEXT.md和相关代码；说明实际读取的ref/文件，并交叉核验 `main` 最新提交与 `NEXT_TASK.md` 中记录的 PR 合并状态是否一致（若 PR 已合并但 `NEXT_TASK.md` 仍标 `REVIEW`，先报告滞后并以真实 `main` 为准，在当前新分支任务实施时一并收敛状态）。保留已有规范，接入时合并必要条款，不覆盖原文件。

当客户端接入 GitHub Remote MCP 出现单文件直读异常（例如 `get_file_contents` 仅返回下载提示与 SHA 而无文本正文，`search_code` 返回空且 `incomplete_results: true`）时，走标准只读降级路径：先列举目录确认路径，再调用 `get_commit(detail="full_patch")` 或 `pull_request_read(method="get_diff")` 读取近期新增或全量重写文件的完整 diff 正文；若目标历史文件未在近期提交全量改动、仅能看到局部 diff 而无法 100% 还原整文件，必须明确报告阻塞并请用户提供全文或补充可还原的历史提交，严禁猜测或伪称已读完整文件。

遵循Karpathy四原则：明确假设与验收条件；复用已有逻辑做最简实现；只精准修改任务涉及之处；实际运行适用验证并如实报告。可逆的日常实现决定在已授权范围内自行推进；关键范围、数据及发布决策由用户确认，不能把日常自主推进扩大为越权。

禁止直接修改main或默认分支。只在独立功能分支工作；合并、部署、发布、公开及删除由用户决定，审核不等于授权执行。不得擅自改许可、影响其他项目、提交秘密或个人隐私。保留安全检查、信任边界验证、错误处理及适用测试，未运行不得写通过。

任务状态为PLANNED / APPROVED / IN_PROGRESS / REVIEW / CHANGES_REQUESTED / ACCEPTED；用户已批准的目标可推进，ACCEPTED仅在用户接受后记录。

## 轻量日常记录

日常只更新 NEXT_TASK.md 作为状态文件（代码和实际需求文档照常修改），包含当前状态、PR或分支、验证结果、未测项、下一步唯一任务及阻塞。因禁止直接修改 `main` 且 PR 提交时标为 `REVIEW`，PR 合并后 `main` 上的 `NEXT_TASK.md` 可能短暂保留合并前快照：用户接受后若尚未合并，可在原 PR 分支先收敛状态；合并后不单独直推 `main`，而是在下一轮接手核验时以真实 `main` 与 PR 实际合并状态为准并在新功能分支首个状态更新中同步修正（或经用户明确批准单独提交状态维护 PR）。详细需求、批准、改动、命令输出、审核意见留在Issue/PR，不为每轮另建任务/审核/交接文件。只有里程碑才归档至docs/handoff/；已有历史记录不改写。

Issue无法写入或读取时，用户提供完整任务；执行端（Codex 或 Antigravity）执行前先在NEXT_TASK.md保存来源、批准与验收所需内容，再在PR补齐详情。可读取已有docs/tasks/历史文件，不强制新建。Antigravity 必须优先从绑定目标 GitHub 仓库的 Project 发起开发会话以获得分支推送与建 PR 权限；若普通会话未挂载仓库导致推送返回 HTTP 403，保留本地提交和 NEXT_TASK 阻塞记录，不伪造 GitHub 链接或声称远端已交付，可按已验证方案导出 `git format-patch` 并附 SHA256 交由 Google Drive 传递，在绑定仓库的 Project 会话核验 SHA256 后用 `git am` 无损恢复提交并推送建 PR。

## 每次新会话的默认 Skill 执行

新项目默认继承 caveman 和 ponytail，每次新会话必须主动读取 `.agents/skills/caveman/SKILL.md` 与 `.agents/skills/ponytail/SKILL.md` 的完整正文并执行适用于本轮的指令，不等用户另行请求。先核对用户当前指令及 PROJECT_CONTEXT.md 中明确记录的禁用决定；只有用户明确禁用的 Skill 才跳过，记录禁用范围，不能把未指定当成禁用。

加载失败（文件缺失、不可读、解析错误、原生调用不可用）必须报告具体 Skill、路径/原因、受影响步骤和未验证项，不得静默跳过或伪称执行。严格区分 Codex CLI 原生 `skills/list` 接口与 Antigravity 等宿主自身的 Skill 发现机制（如 `list_skills` / `lookup_skills`）：不得因缺少 `codex` CLI 就断言宿主不支持原生 Skill，也不得将宿主内置 Skill 注册表混淆为 Codex `app-server` `skills/list`；无宿主发现机制的环境（如纯对话规划端 Gemini）读取全文后标明“按文件指令执行”，严禁冒充原生发现或自动激活；无法读取全文（含 MCP 单文件直读异常且无法从 diff 完整还原）时暂停依赖该 Skill 的步骤并如实报告，按已有安全/授权规范处理任务。

交接必须按四级证据分开记录：1）原生发现（区分记录 Codex CLI `skills/list` 结果与 Antigravity 等宿主自身 Skill 发现结果；未安装 `codex` CLI 仅写明未运行 Codex `skills/list`，不等于宿主不支持原生 Skill；确无发现机制才写不支持）；2）正文读取（实际读取 `.agents/skills/*/SKILL.md` 的路径与方式）；3）按文件指令执行（本轮实际遵循的具体行为证据）；4）新会话自动激活（未实测一律写未验证）。发现或文件存在不等于实际执行；本规则是每次会话主动加载的要求，不是自动激活已经实测的声明。

简短风格和最小改动不能削弱原有开发、安全、测试、授权与交接规范；持久文档保持完整清晰。用户语言/回复格式和更高优先级规则仍优先。禁止擅自安装上游hooks、代理、遥测或全局配置。

## 框架仓库维护

本仓库为手机优先的AI Dev Handoff文档/模板框架，零运行时依赖。规范模板是用户项目初始化的来源，修改时同步相关初始化提示，不重复堆叠规则。运行 `python3 scripts/validate.py`、`python3 scripts/test_validate.py`、`python3 scripts/verify_repo_skills.py` 与 `git diff --check`；原生宿主兼容性变化且具备 `codex` CLI 时另跑 `python3 scripts/verify_repo_skills.py --host`（该参数专测 Codex `app-server` `skills/list`，无 `codex` CLI 的宿主如实记录未运行该 Codex 专有探测，不断言宿主无自身 Skill 机制）。保留原始第三方文件和许可，根项目许可仍由所有者决定。
