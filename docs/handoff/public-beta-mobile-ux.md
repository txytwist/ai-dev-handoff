# Issue #7 Public Beta 手机体验 Handoff

## Status
REVIEW，等待 ChatGPT 审核。

## Repository and refs
`txytwist/ai-dev-handoff`；基线 `main@aeeef57`；分支 `feat/public-beta-mobile-ux`。最终head以PR和最终回复为准，避免自引用。读取时仓库已Public，本次未修改设置。

## Source and approval
[任务与批准记录](../tasks/public-beta-mobile-ux.md)，对应 Issue https://github.com/txytwist/ai-dev-handoff/issues/7 。

## Changes
- 当前README/初始化/完整引导/外部评审/日常指南/贡献/安全/Beta说明改为Public Beta，保留许可待定、实机未验收，公开材料直接复制，无需索取或Fork。
- 双语README把完整引导与设置链接提到状态说明之前，五角色改短段，不再用三列表。
- 两张Mermaid改中文短标签，完整中英文文字仍在图后；保留批准、持久任务与权限回退、主动交接、返工回批准与合并另授权。
- 新增可重复四档窄屏模拟脚本与说明；真实iPhone极简视觉清单全为NOT_RUN，原端到端未实测状态未勾选。
- 当前指南新增过时Private文案回归检查。旧tasks/Handoff正文原样保留，仅索引标记历史快照。

## Acceptance criteria
静态检查与本地模拟已执行；公开分支可读性在推送后核实。Public Beta不等于开源授权或实机验收。未改许可证，未合并/部署/更改可见性，未操作其他项目。

## Evidence
2026-11-20 实际执行并退出0：

```text
python3 scripts/validate.py
PASS: 41 required files; 37 Markdown files; 86 local links; shared template fields; states; 38 files scanned for common sensitive patterns.
python3 scripts/test_validate.py
PASS: clean fixture accepted; missing file/workflow, broken link, missing field and synthetic token and stale private onboarding rejected; temporary fixture removed.
PASS: privacy scanner detects synthetic token/email; flags non-UTF8 as unscanned; accepts ordinary text.
git diff --check
无输出，通过。
node scripts/check_mobile.mjs /tmp/ai-dev-handoff-mermaid /usr/bin/chromium /tmp/handoff-mobile-results
16项PASS，JSON与截图输出到临时目录。
```

实际环境：Node 24.22.1，Mermaid 11.17.2，marked 4.3.0，Puppeteer 23.11.1，Chromium 156.0.8078.79，deviceScaleFactor=1，viewport高度812px。工具仅在临时目录，复现安装/命令见模拟说明。

| viewport宽 | 两个README页面宽 | 完整引导Y | 图1宽 / 图2宽 | 图2最小有效字px |
| --- | --- | --- | --- | --- |
| 320 | 320，无溢出 | 222.31 | 236.52 / 288 | 13.71 |
| 375 | 375，无溢出 | 222.31 | 236.52 / 336.22 | 16 |
| 390 | 390，无溢出 | 222.31 | 236.52 / 336.22 | 16 |
| 430 | 430，无溢出 | 222.31 | 236.52 / 336.22 | 16 |

两图均由真实Mermaid解析/渲染器生成，图1有效字约16px。已人工查看320px的中英文README和图2截图；其余宽度以脚本测量为证据，不声称逐台实机走查。截图/JSON未提交，可通过脚本再生成。

匿名公开读取与远端Actions待推送/PR后核对，结果以PR对应head为准。

## PR and paths
PR创建后补回。主要指南位于根README/START_HERE/CHATGPT_SETUP及docs；模拟复现见 [mobile-simulation](../mobile-simulation.md)，实机待办见 [检查单](../mobile-acceptance.md)。

## Limitations
模拟使用marked GFM与简化CSS，不是GitHub生产CSS；Chromium不是Safari或GitHub App。字形、字体、复制功能、实际GitHub图形版本与界面仍需真实iPhone检查，NOT_RUN保持不变。历史审计中的私有状态与旧测试数是当时快照，不按当前状态改写。

## Next action
用户将PR/最新head带回ChatGPT审核。然后在自己的iPhone实际GitHub页面完成极简视觉清单，报告设备/版本、链接/ref与问题位置。接受、合并及许可由用户单独决定。
