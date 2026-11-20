# Issue #5 对比图表交接

## Status
REVIEW，等待 ChatGPT 审核。

## Repository and refs
`txytwist/ai-dev-handoff`；基线 `main@e86d523`，分支 `feat/role-workflow-comparison`。最终 head 以 PR 和最终回复为准。

## Source and approval
[任务与批准记录](../tasks/role-comparison.md)，对应 Issue https://github.com/txytwist/ai-dev-handoff/issues/5 。

## Changes
README中英文增加五行简洁角色对比表，放在原手机入口链接之后；详细图表留在工作流页，避免首页长图。START_HERE只加一行价值说明。工作流新增两张短标签双语纵向 Mermaid与等价文字，明确典型示例、权限回退、用户主动切换、返工批准、接受不自动合并。

## Acceptance criteria
中英文角色、流程与边界对应；入口仍在表格之前；只改文档与本次记录。外部测试矩阵状态、仓库设置和许可证未修改。语法检查与实际渲染限制见证据。

## Evidence
2026-11-20 实际运行，以下均退出 0：

```text
python3 scripts/validate.py
PASS: 37 required files; 34 Markdown files; 78 local links; shared template fields; states; 35 files scanned for common sensitive patterns.
python3 scripts/test_validate.py
PASS: clean fixture accepted; missing file/workflow, broken link, missing field and synthetic token rejected; temporary fixture removed.
PASS: privacy scanner detects synthetic token/email; flags non-UTF8 as unscanned; accepts ordinary text.
git diff --check
无输出，通过。
```

Mermaid临时工具仅装在 `/tmp/ai-dev-handoff-mermaid`，不写入项目依赖。安装命令：`PUPPETEER_SKIP_DOWNLOAD=1 npm install --prefix /tmp/ai-dev-handoff-mermaid --no-audit --no-fund @mermaid-js/mermaid-cli@11.4.2`，另装 `jsdom@26.1.0`。实际 Mermaid解析器版本为 11.17.2。

从 docs/workflow.md 提取两个 Mermaid块后，运行 `node /tmp/ai-dev-handoff-mermaid/check.mjs`，两图均返回 `PASS, diagramType=flowchart-v2`；该临时脚本用 JSDOM 提供 DOM、调用 mermaid.parse 检查。初次 `mmdc` 加载本地 HTML 被 Chromium环境策略拦截（ERR_BLOCKED_BY_ADMINISTRATOR），未将该尝试记为通过。

改用内存文档的本地渲染脚本 `node /tmp/ai-dev-handoff-mermaid/render.mjs`：Puppeteer设置 375×812 视口，加载 mermaid.min.js 内容并调用 mermaid.render，生成 SVG/截图。两图成功；首图实际宽 294.75px、第二图宽 359px（可用内容区），截图人工检查无文字截断。双语分行、纵向排布，流程图2的返工返回规划与范围批准节点。临时工具和截图未提交；不添加项目运行时依赖。

PR创建后检查对应 head 的 GitHub Actions `documentation`，远端结果以真实 run 为准。

## PR and paths
PR创建后补回；README.md、README.zh-CN.md、START_HERE.md、docs/workflow.md，及本任务/交接记录。

## Limitations
示意内容不是性能数据或真实使用验收；本地 Mermaid 11.17.2/Chromium 渲染通过，但未直接验证 GitHub当前 Mermaid版本的页面渲染，也未进行真实 iPhone实测。README三列表在窄屏可能需横向滑动，主启动链接置于表前，详情图与等价文字放在工作流页。没有部署、合并、改可见性或许可。

## Next action
用户把 PR、最新 head 和交接返回 ChatGPT审核；决定接受或修改，合并需另授权。
