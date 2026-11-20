# 可重复的窄屏模拟（维护者）

普通手机用户不需安装任何工具。以下是本地验证，不是 GitHub真实页面或 iPhone Safari/App 实测。项目无运行时依赖；临时 Node工具只在维护者测试目录安装，不加入 package.json/锁文件。

```sh
PUPPETEER_SKIP_DOWNLOAD=1 npm install --prefix /tmp/handoff-mobile-tools --no-audit --no-fund mermaid@11.17.2 puppeteer@23.11.1 marked@4.3.0
node scripts/check_mobile.mjs /tmp/handoff-mobile-tools /usr/bin/chromium /tmp/handoff-mobile-results
```

需要已安装的 Node（建议22+）、Chromium（替换为实际可执行路径）与 npm下载权限。输出目录包含 JSON和16张截图，不提交依赖/截图到仓库。测试用 `marked` GFM解析 README，以简化的16px字体、16px边距模拟文档布局；**不是 GitHub生产 CSS 或实际 iOS字体**。Mermaid用默认 strict模式的真实解析器/渲染器。保留等价文字，即使客户端不渲染图也可读。

脚本在 320、375、390、430px ×812px 测量：README无页面横向溢出、无表格、五个角色小节，完整引导链接在第一屏；两图无页面溢出、适配内容区，节点字体缩放后至少12px。失败会非零退出。数字阈值不是人类可读性认证，截图仍需人工查看；GitHub App、移动浏览器与真实iPhone按 [NOT_RUN检查单](mobile-acceptance.md) 验收。

每次改动后保存实际版本、viewport、输出与失败项到 Handoff；不得把模拟通过写成实机验收通过。现有 CI 仍只跑标准库静态校验，不依赖 npm或浏览器。
