# H5 / HTML PPT 技术调研与 Spotify 风格设计指南

> 调研与制作日期：2026-10-17  
> 目标：为课程类演示制作一份可离线打开、可键盘控制、带交互组件的精美网页演示。本文中的“Spotify 风格”仅指绿色、黑色、白色、高对比排版和音乐节奏感的视觉借鉴，不复制 Spotify 商标、Logo、专有字体或产品界面。

## 1. 视觉基调：绿黑与绿白

### 1.1 从 Spotify 公开设计材料提炼出的可用特征

Spotify 的公开设计内容强调一致的设计系统、可复用设计语言、明确的品牌资产使用边界，以及在不同产品与场景中保持统一体验。落到演示网页，可提炼为以下视觉方法：

- **高对比主色**：深黑作为舞台，鲜绿色作为行动、进度和关键结论；浅色页反转为白底、黑字、绿色结构块。
- **大字号、少文本**：标题占据主要视觉面积，每页只保留一个明确观点。
- **圆形与节奏元素**：使用唱片、音轨、均衡器、波形和圆角胶囊作为抽象装饰，不直接复制产品 UI。
- **强层级**：超大标题、短标签、紧凑正文三层即可，避免过多卡片和边框。
- **动效有节拍但不炫技**：进度条、分步出现、状态切换使用 180–500ms 的短动效；遵守 `prefers-reduced-motion`。
- **绿色表示“可执行/已验证”**，红色只用于冲突或危险操作，灰色用于尚未验证。

### 1.2 本项目设计令牌

```css
--spotify-green: #1ed760;
--spotify-green-strong: #1fdf64;
--ink: #0a0a0a;
--surface-dark: #121212;
--paper: #f7f7f2;
--white: #ffffff;
--muted-dark: #a7a7a7;
--danger: #ff5c5c;
--warning: #ffd166;
```

字体使用本机中文无衬线字体栈，避免未经授权分发 Spotify 专有字体：

```css
font-family: Inter, "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC", Arial, sans-serif;
```

### 1.3 版式规则

1. 16:9 观感优先，但页面使用 `100dvh`，可适配会议共享和移动设备。
2. 标题控制在 8–18 个汉字；正文每页不超过 80–120 个汉字。
3. 黑底页用于开场、结论和情绪推进；白底页用于流程、数据和代码；绿底页用于转场或行动号召。
4. 每页只保留一个主交互，避免演示者同时操作多个控件。
5. 绿色高亮面积不宜超过页面约 35%，否则会失去强调作用。

## 2. GitHub 上值得关注的 H5 / HTML PPT 技术

| 方案 | 内容格式 | 交互能力 | 导出/交付 | 适合场景 | 本项目判断 |
|---|---|---|---|---|---|
| [Slidev](https://github.com/slidevjs/slidev) | Markdown + Vue + Vite | 很强，可直接写 Vue 组件、动画和代码演示 | HTML、PDF、PPTX 等 | 技术演讲、长期维护、多文件课程 | **首选工程化方案** |
| [reveal.js](https://github.com/hakimel/reveal.js) | HTML 或 Markdown | 很强，Fragments、Auto-Animate、插件、演讲者视图成熟 | 静态网页、PDF | 通用演示、需要成熟演讲功能 | **首选通用框架** |
| [Marp CLI](https://github.com/marp-team/marp-cli) | Markdown + CSS | 中等，偏线性演示 | HTML、PDF、PPTX | 快速把讲义转成幻灯片 | 内容优先时合适 |
| [PPTist](https://github.com/pipipi-pikachu/PPTist) | Vue + TypeScript 可视化编辑器 | 很强，接近在线 PowerPoint 编辑体验 | 项目内支持多种导入/导出能力 | 需要让用户在线编辑幻灯片 | 功能强但集成成本高 |
| [Spectacle](https://github.com/FormidableLabs/spectacle) | React / JSX | 强，可组合 React 组件 | Web | React 团队、产品演示 | React 技术栈可选 |
| [WebSlides](https://github.com/webslides/WebSlides) | HTML + CSS | 基础 | Web | 轻量静态 H5 演示 | 可参考版式，不作为新项目首选 |

### 2.1 Slidev 的生成与定制方法

```bash
npm init slidev@latest
cd your-slidev-project
npm run dev
```

核心文件通常是 `slides.md`。每个 `---` 分隔一页；Frontmatter 控制主题、布局、代码高亮等。需要交互时直接在 Markdown 中嵌入 Vue 组件：

```md
---
theme: default
title: Agent 协作实验室
---

# 流畅 ≠ 正确

<FactChecker :facts="facts" />
```

推荐目录：

```text
slides.md
components/
  FactChecker.vue
  ToolTrace.vue
styles/
  index.css
public/
```

适合加入：可点击流程图、代码执行模拟、实时问答、计时器、拖拽排序、ECharts/D3 图表、视频与音频。

### 2.2 reveal.js 的生成与定制方法

最小结构是 `.reveal > .slides > section`。使用 `fragment` 控制分步出现，用 `data-auto-animate` 连接前后两页，用插件增强 Markdown、代码、数学公式和演讲者备注。

```html
<div class="reveal">
  <div class="slides">
    <section>
      <h1>流畅 ≠ 正确</h1>
      <p class="fragment">先看初稿</p>
      <p class="fragment">再看工具证据</p>
    </section>
  </div>
</div>
```

当需要成熟的键盘导航、URL 定位、演讲者视图、插件生态和 PDF 打印时，reveal.js 很合适。若内容交互只是按钮、切换、输入模拟，也可以直接使用原生 JavaScript。

### 2.3 Marp 的使用方法

Marp 适合“已有 Markdown 讲义 → 快速生成幻灯片”。用 Frontmatter 配主题，用 CSS 自定义颜色和字号：

```md
---
marp: true
theme: spotify-course
paginate: true
---

# Agent 协作实验室

人定义目标，Agent 协助，Java 工具提供事实。
```

```bash
npx @marp-team/marp-cli slides.md --html
npx @marp-team/marp-cli slides.md --pptx
```

它适合内容稳定、交互要求不高、同时需要 PPTX/PDF 的场景；复杂交互仍建议 Slidev、reveal.js 或自定义网页。

## 3. GitHub 上的“生成前端幻灯片”Skills

### 3.1 frontend-slides-skills

- 仓库：[zarazhangrui/frontend-slides-skills](https://github.com/zarazhangrui/frontend-slides-skills)
- 定位：让 Coding Agent 生成单文件 HTML 幻灯片，内置多种主题、组合预设、键盘导航和缩略图等演示能力。
- 常见安装方式：把 Skill 克隆或复制到 Agent 的 skills 目录；部分 Agent 可通过 Skills CLI 安装。
- 常见调用方式：使用 `/slides` 或在提示中明确要求“生成单文件 HTML 演示、指定主题、页数、内容来源和交互”。

推荐提示模板：

```text
请根据 docs/课程方案.md 生成 12 页单文件 HTML 演示。
视觉：绿色、黑色、白色，高对比，大标题，音乐节奏感；不要复制品牌 Logo。
交互：键盘翻页、进度条、目录总览、事实核验按钮、搜索工具模拟、评分计算器。
交付：离线可用，不依赖 CDN；打印时每页单独分页。
```

### 3.2 第三方 Skill 的安全使用建议

1. 安装前阅读 `SKILL.md`、脚本和依赖，确认没有上传文件、读取密钥或执行高风险命令。
2. 优先固定到明确 commit，而不是长期跟随不受控的 `main`。
3. 在独立分支或工作区试运行，检查生成文件和命令记录。
4. Skill 负责“流程和规范”，最终生成质量仍由内容结构、设计约束和验收标准决定。
5. 若只需要一份独立 H5 演示，单文件 HTML 往往比引入完整框架更易交付；若要持续迭代、多人维护，选择 Slidev 或 reveal.js。

## 4. 本次交付采用的实现路线

本次演示采用**零依赖、单文件 HTML**，原因：

- 双击即可离线打开，适合教室和腾讯会议共享；
- 不依赖 npm、CDN 或网络；
- 能精确实现课程所需的交互，而不引入框架体积；
- 后续可平滑迁移到 reveal.js 或 Slidev。

已实现的交互：

- 左右方向键、空格、PageUp/PageDown 翻页；
- 进度条、页码、章节点导航；
- `O` 总览、`H` 帮助、`N` 演讲者备注、`F` 全屏；
- 触摸滑动；
- Agent 初稿问题点击标注；
- 事实核验动画与计数变化；
- Java 搜索工具修复前后切换；
- 可操作的库存搜索与低库存模拟；
- 高风险操作判断题；
- 评分计算器；
- 可保存到浏览器本地的课后任务清单；
- 打印分页与减少动效支持。

## 5. 后续升级建议

### 路线 A：继续保持单文件

适合一次性授课。继续新增数据时，把数据放进页面底部的 JavaScript 对象；不要把所有文字堆进页面，应增加页数。

### 路线 B：迁移到 reveal.js

把每个 `.slide` 转成 `<section>`，保留内部 HTML、CSS 和互动组件；导航、备注和 PDF 导出交给 reveal.js。

### 路线 C：迁移到 Slidev

把内容拆成 `slides.md`，将库存实验、事实核验和评分器改为 Vue 组件。适合后续 16 周课程持续维护，并为每周建立独立章节。

## 6. 主要参考链接

- Spotify Design：<https://spotify.design/>
- Spotify Developer Design Guidelines：<https://developer.spotify.com/documentation/design>
- Slidev：<https://github.com/slidevjs/slidev>
- Slidev 文档：<https://sli.dev/>
- reveal.js：<https://github.com/hakimel/reveal.js>
- reveal.js Fragments：<https://revealjs.com/fragments/>
- reveal.js Auto-Animate：<https://revealjs.com/auto-animate/>
- reveal.js Speaker View：<https://revealjs.com/speaker-view/>
- Marp CLI：<https://github.com/marp-team/marp-cli>
- PPTist：<https://github.com/pipipi-pikachu/PPTist>
- Spectacle：<https://github.com/FormidableLabs/spectacle>
- WebSlides：<https://github.com/webslides/WebSlides>
- frontend-slides-skills：<https://github.com/zarazhangrui/frontend-slides-skills>


