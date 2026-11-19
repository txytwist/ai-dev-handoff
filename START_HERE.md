# 📱 手机上开始

每次只完成当前一步，再让 ChatGPT 给下一步。普通用户不需要终端、SSH、电脑、服务器或独立 API。按钮位置会随版本变化；本项目没有实测当前 iPhone UI，以下按功能描述，不承诺固定标签。

## 先准备访问条件

1. 在手机确认你能使用 ChatGPT、GitHub 和 Cloud Codex。可用性和额度依账户而定；任一服务不可用时先解决访问，不声称工作流已经启动。
2. 在 ChatGPT 打开或创建用于目标项目的 Project，找到项目指令功能，保存 [CHATGPT_SETUP.md](CHATGPT_SETUP.md) 的初始化块。若账户没有 Project 功能，可在每个新会话重新粘贴初始化块与最新上下文，不能承诺持久记忆。
3. 提供本框架 README 和初始化文档的可访问链接。私有仓库需要授权 GitHub 连接；不能读取时复制正文。让 ChatGPT 回报实际读取的文件和 ref；单独输入项目名不会加载文件。
4. 告诉 ChatGPT 选择下列 A 或 B。下一步只走对应路线。

## A：创建新项目

1. 告诉 ChatGPT 项目目标、名称和希望看到的最小结果。先让它检查实际 GitHub 读、写 Issue、写文件、建仓能力及授权，能力不能互相推定。
2. 有建仓能力且你已授权时，可由 ChatGPT 建独立 Private 仓库。已知无建仓权限时，不要交给 Codex 重试：手机浏览器打开 https://github.com/new ，选择你的账号，填写项目名，选择 Private，添加 README，创建一次。然后让 ChatGPT/Codex 的 GitHub 连接获得该仓库访问权。不要复制凭据进聊天。
3. 给 ChatGPT 新仓库链接。让它提出最小初始化计划：用 [项目上下文模板](templates/PROJECT_CONTEXT.md) 建立 `PROJECT_CONTEXT.md`，用 [规则模板](templates/AGENTS.md) 建立 `AGENTS.md`，添加 `docs/handoff/README.md`（说明存放路径与状态规则）。批准后有写文件能力的 ChatGPT执行；无能力时交 Codex按该计划创建，走功能分支和 PR。
4. 让 ChatGPT 规划一个小任务，展示目标、范围、验收和风险。你明确同意后，ChatGPT 优先在**新项目仓库**创建 Issue；不能写时生成完整 [任务](templates/TASK_TEMPLATE.md)，按 [Codex 备选指令](CODEX_SETUP.md) 交接。
5. 在手机打开 Cloud Codex，选择该项目仓库，检查仓库名与分支，粘贴指定 Issue 的执行指令。要求先回报实际读取的任务标题、编号及规范文件。若读不到，提供任务全文或 `docs/tasks/` 路径。
6. 之后按 [日常速查](docs/mobile-quickstart.md) 返回 ChatGPT 审核。

## B：接入已有项目

1. 给 ChatGPT 你的现有项目仓库链接。让它先读取 README、目录、AGENTS.md 和已有开发/交接规则，说明读取的 ref；读不到时提供这些文件和目录清单。
2. 要求一份保留已有程序的接入计划：只补缺失的上下文和交接索引，已有 `AGENTS.md` 只提议合并必要条款，冲突先报告。不要覆盖现有规范，不要 Fork 框架替代项目。
3. 批准计划后，由有写权限的 ChatGPT 或你授权的 Codex 在功能分支添加必要文件，提交 PR；接入本身也需要审核，不能顺手合并。
4. 在**现有项目仓库**规划并批准下一任务，由 ChatGPT 优先创建 Issue；使用同样的 Codex 执行与审核流程。

## 一次设置，后续复用

每个独立项目设置一次；新会话仍应确认项目指令与最新上下文已载入。之后只需要任务、PR、交接记录和审核，不需要反复安装框架或 Skill。先阅读 [完整示例](examples/complete-cycle.md) 看一次往返。
