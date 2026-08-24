<p align="center">
  <img src="./assets/sanhsien-banner-github-readme-1280x320.png" alt="San-Hsien Yang — Practical tools. Thoughtful automation. 實用工具，務實自動化。" width="100%">
</p>

# SanHsien

I build practical, Windows-first tools and AI-assisted workflows — local-first, with clear boundaries and verifiable releases. Every project starts from a real workflow problem and ends at something people can actually download and run.

我做實用的 Windows 優先工具與 AI 協作流程，重視本機優先、清楚邊界、可驗證交付。每個專案都從實際的工作流程痛點出發，做到能下載、能執行為止。

## Featured Projects / 精選作品

### [OpenShelf](https://github.com/SanHsien/openshelf)

Batch-export books you legally own in Google Play Books: DRM-free titles download as EPUB/PDF, protected ones keep the official `.acsm` handoff for Adobe Digital Editions.
批次匯出自己合法擁有的 Google Play 圖書：無 DRM 的直接下載 EPUB/PDF，受保護的保留官方 `.acsm` 交接流程。

`Python` `Playwright` `httpx` `Desktop GUI` `Local-first`

### [GPT AI Assistant](https://github.com/SanHsien/gpt-ai-assistant)

Self-hosted personal AI assistant inside LINE — chat, voice, vision, search, schedules, tasks, reminders, weather — on your own OpenAI, LINE, and Supabase credentials. "AI finished" and "LINE delivered" are separate checkpoints, so a delivery retry never re-runs paid AI work.
可自架的 LINE 個人 AI 助理：聊天、語音、圖片、搜尋、行程、任務、提醒、天氣，全跑在自己的帳號上。「AI 已完成」與「LINE 已送達」是兩個 checkpoint，送達重試不會重跑已付費的 AI 工作。

[Documentation site / 文件站](https://sanhsien.github.io/gpt-ai-assistant-docs/) · Derived from `memochou1993/gpt-ai-assistant`, independently maintained.

`JavaScript` `Node.js 24` `Vercel` `Supabase` `LINE Messaging API` `Google Calendar / Tasks`

### [聲成文 VoxProse](https://github.com/SanHsien/voxprose)

Local-first voice typing for Windows: hotkey recording, on-device Faster-Whisper transcription, optional LLM rewriting and translation, typed straight into the focused app.
Windows 本機語音輸入：快捷鍵錄音、本機 Faster-Whisper 辨識、可選 LLM 潤飾與翻譯，直接輸入目前作用中的程式。

Derived from VoiceType4TW, independently maintained.

`Python` `PyQt6` `Faster-Whisper` `CUDA` `Windows`

### [ChannelDepot](https://github.com/SanHsien/channeldepot)

Portable YouTube channel archiving with GUI and CLI: batch workflows, filters, ffmpeg integration, and content the signed-in user is already authorized to watch.
可攜式 YouTube 頻道保存工具，GUI 與 CLI 並具：批次工作流、篩選、ffmpeg 整合，也支援登入者原本就有權觀看的內容。

`Python` `yt-dlp` `Tkinter` `ffmpeg` `Windows / macOS / Linux`

### [VoxAvatar](https://github.com/SanHsien/voxavatar)

Windows VRM desktop companion that turns an AI assistant's playback into lip sync, motion, states, and message bubbles; compatible agents drive it over a loopback-only MCP server.
Windows VRM 桌面角色：把 AI 助理的聲音轉成口型、動作、狀態與訊息氣泡，相容 Agent 可經僅限本機的 MCP 控制。

Derived from `xikhar/persona`, independently maintained.

`TypeScript` `Electron` `Three.js` `VRM / VRMA` `MCP`

## Agent Skills & Tooling / Agent 技能與開發套件

Developer-facing work for AI coding agents — original engineering references and independently maintained Windows-first forks, aimed at agent workflows rather than at general users.
給 AI coding agent 的開發向作品：原創工程參考專案與 Windows-first 維護型 fork，服務 agent 工作流，不是一般使用者下載即用的 App。

**AI coding governance stack ｜ AI coding 治理堆疊** — four repos constraining agents at four layers, each usable on its own. 四個 repo 分別約束 agent 的四個層面，也可以單獨使用。

| Layer / 層 | Repo | |
| --- | --- | --- |
| Dispatch / 派工決策 | [agent-advisor](https://github.com/SanHsien/agent-advisor) | Risk-gated routing across four agent runtimes ｜四種 agent runtime 的風險分流路由 |
| Execution / 動作攔截 | [harness-guard](https://github.com/SanHsien/harness-guard) | Runtime hooks blocking dangerous commands, unevidenced completion claims, commits over failing tests ｜攔截危險指令、無證據的完成宣稱、紅燈仍提交 |
| Output / 產出品質 | [ai-quality-gates](https://github.com/SanHsien/ai-quality-gates) | Gherkin specs, coverage and mutation gates, architecture contracts, bounded agent-loop policy ｜可執行規格、覆蓋率與 mutation gate、架構契約、有界 loop policy |
| Delivery / 交付流程 | [paulsha-cortex](https://github.com/SanHsien/paulsha-cortex) | Candidate, verification, independent review, completion evidence ｜候選、驗證、獨立審查與完成證據 |

**Other agent tooling ｜ 其他 agent 工具**

| Repo | | |
| --- | --- | --- |
| [MyR2D2](https://github.com/SanHsien/MyR2D2) | Ten Claude Code skills against session amnesia: save-and-verify before shutdown, handoff and pickup between sessions, daily and weekly debriefs, self-check before reporting, and second review by a different model ｜十支對抗 session 失憶的 skills：收工前落地並驗證、跨 session 交接與接手、日結週結、回報前自檢，以及交給另一個模型的二審 | `Python` fork of [`tingyulu/MyR2D2`](https://github.com/tingyulu/MyR2D2) |
| [opencodex](https://github.com/SanHsien/opencodex) | Universal provider proxy — run Codex or Claude Code on Claude, Gemini, Grok, DeepSeek, or local Ollama, native model picker intact ｜通用供應商代理，讓 Codex／Claude Code 改用任何 LLM，選擇器仍是原生的 | `TypeScript` fork of [`lidge-jun/opencodex`](https://github.com/lidge-jun/opencodex) |
| [agentdeck](https://github.com/SanHsien/agentdeck) | Windows tray cockpit: quota monitoring, multi-model roundtable, subagent roles, HTML reports; quota read from local files only ｜系統匣控制台：額度監看、多模型圓桌、subagent 角色、HTML 報告，額度只讀本機檔案 | `Python` fork of `aqua5230/usage` |
| [book-to-skill](https://github.com/SanHsien/book-to-skill) | Turn a technical book or docs folder into on-demand Agent Skills — load the relevant chapter, not the whole book ｜把技術書或文件夾轉成按需載入的 Agent 技能，只載入用得到的那一章 | `Python` fork of [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) |

[Browse all public repositories →](https://github.com/SanHsien?tab=repositories&q=&type=public&language=&sort=)

## How I Work / 工作方式

- **Local-first by default** ｜**預設本機優先** — if it runs on the user's machine, it does not get a hosted backend first.
- **Release-oriented** ｜**以交付為導向** — downloadable, runnable, verifiable beats a demo.
- **Privacy-aware** ｜**重視隱私邊界** — user files, images, and tokens do not go to services that do not need them.
- **Explicit boundaries** ｜**寫明邊界** — licensing, platform rules, unsupported cases, and operational risks are stated, not implied.
- **AI-assisted, still verified** ｜**AI 協作但仍要驗證** — agents speed up prototyping and docs; releases still need tests, packaging, and stated limits.

Recurring themes across the projects: bringing AI into interfaces people already use, and automating repetitive media, document, and operational work.
專案共通的主題：把 AI 放進使用者本來就在用的介面，以及把媒體、文件與日常作業的重複工作自動化。

## Earlier & Private Work / 過往與非公開作品

Excel/VBA business automation, Palm and Android field applications, web-based submission and review systems, and internal operational tools. Private and organizational projects are described by capability only.
Excel/VBA 營運自動化、Palm 與 Android 行動程式、線上填報／審查系統、組織內部作業工具。私人或組織型專案僅描述能力，不公開可識別資訊與正式資料。

## Tools / 工具

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=111)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-306998?logo=python&logoColor=white)

## Elsewhere / 其他平台

- [LinkedIn](https://www.linkedin.com/in/sanhsien/) — professional profile / 專業檔案
- [Facebook](https://www.facebook.com/sanhsien) · [Instagram](https://www.instagram.com/sanhsien/) · [Threads](https://www.threads.com/@sanhsien) · [X](https://x.com/Hsien_3)
