<p align="center">
  <img src="./assets/sanhsien-banner-github-readme-1280x320.png" alt="San-Hsien Yang — Practical tools. Thoughtful automation. 實用工具，務實自動化。" width="100%">
</p>

# SanHsien

I build and maintain practical, local-first tools and AI workflows—Windows-first when desktop integration matters. My public work spans desktop utilities, self-hosted assistants, browser tools, and agent governance tooling.

我打造並維護實用的本機優先工具與 AI 工作流程；需要桌面整合時以 Windows 優先。公開作品涵蓋桌面工具、自架助理、瀏覽器工具，以及 agent 治理工具。

## Featured Projects / 精選作品

### [OpenShelf](https://github.com/SanHsien/openshelf)

Batch-export books you legally own in Google Play Books: DRM-free titles download as EPUB/PDF, protected ones keep the official `.acsm` handoff for Adobe Digital Editions.
批次匯出自己合法擁有的 Google Play 圖書：無 DRM 的直接下載 EPUB/PDF，受保護的保留官方 `.acsm` 交接流程。

`Python` `Playwright` `httpx` `Desktop GUI` `Local-first`

### [GPT AI Assistant](https://github.com/SanHsien/gpt-ai-assistant)

Self-hosted personal AI assistant inside LINE — chat, voice, vision, search, schedules, tasks, reminders, weather — on your own OpenAI, LINE, and Supabase credentials. "AI finished" and "LINE delivered" are separate checkpoints, so a delivery retry never re-runs paid AI work.
可自架的 LINE 個人 AI 助理：聊天、語音、圖片、搜尋、行程、任務、提醒、天氣，全跑在自己的帳號上。「AI 已完成」與「LINE 已送達」是兩個 checkpoint，送達重試不會重跑已付費的 AI 工作。

[Documentation site / 文件站](https://sanhsien.github.io/gpt-ai-assistant-docs/) · Derived from [`memochou1993/gpt-ai-assistant`](https://github.com/memochou1993/gpt-ai-assistant), independently maintained.
衍生自 [`memochou1993/gpt-ai-assistant`](https://github.com/memochou1993/gpt-ai-assistant)，獨立維護。

`JavaScript` `Node.js 24` `Vercel` `Supabase` `LINE Messaging API` `Google Calendar / Tasks`

### [ChatGPT Sidebar](https://github.com/SanHsien/chatgpt-sidebar)

Chrome MV3 side panel that embeds the ChatGPT session already signed in on the browser, builds Traditional Chinese prompts from the current page or selection (summary, translate, explain, outline), and inserts them without auto-submit.
Chrome MV3 側邊欄擴充功能：嵌入瀏覽器裡已登入的 ChatGPT，依目前頁面或選取文字組成繁中提示詞（摘要／翻譯／解釋／大綱），只寫入輸入框、不自動送出。

[Chrome Web Store / Chrome 線上應用程式商店](https://chromewebstore.google.com/detail/chatgpt-sidebar-embedded/kilnbieekgofpkgbhohmogcjkebfflkd)

`JavaScript` `Chrome MV3` `Side Panel` `Local-first`

### [聲成文 VoxProse](https://github.com/SanHsien/voxprose)

Local-first voice typing for Windows: hotkey recording, on-device Faster-Whisper transcription, optional LLM rewriting and translation, typed straight into the focused app.
Windows 本機語音輸入：快捷鍵錄音、本機 Faster-Whisper 辨識、可選 LLM 潤飾與翻譯，直接輸入目前作用中的程式。

Derived from [`jfamily4tw/voicetype4tw-mac`](https://github.com/jfamily4tw/voicetype4tw-mac), independently maintained.
衍生自 [`jfamily4tw/voicetype4tw-mac`](https://github.com/jfamily4tw/voicetype4tw-mac)，獨立維護。

`Python` `PyQt6` `Faster-Whisper` `CUDA` `Windows`

### [ChannelDepot](https://github.com/SanHsien/channeldepot)

Portable YouTube channel archiving with GUI and CLI: batch workflows, filters, ffmpeg integration, and content the signed-in user is already authorized to watch.
可攜式 YouTube 頻道保存工具，GUI 與 CLI 並具：批次工作流、篩選、ffmpeg 整合，也支援登入者原本就有權觀看的內容。

`Python` `yt-dlp` `Tkinter` `ffmpeg` `Windows / macOS / Linux`

### [VoxAvatar](https://github.com/SanHsien/voxavatar)

Windows VRM desktop companion that turns an AI assistant's playback into lip sync, motion, states, and message bubbles; compatible agents drive it over a loopback-only MCP server.
Windows VRM 桌面角色：把 AI 助理的聲音轉成口型、動作、狀態與訊息氣泡，相容 Agent 可經僅限本機的 MCP 控制。

Derived from [`xikhar/persona`](https://github.com/xikhar/persona), independently maintained.
衍生自 [`xikhar/persona`](https://github.com/xikhar/persona)，獨立維護。

`TypeScript` `Electron` `Three.js` `VRM / VRMA` `MCP`

## Developer Workflows & Agent Tooling / 開發工作流程與 Agent 工具

Developer-facing tools and engineering references for AI-assisted development, including original projects and clearly attributed maintenance forks.
給 AI 輔助開發使用的工具與工程參考，包含原創專案與清楚標示上游來源的維護型 fork。

**AI governance ｜AI 治理** — the recurring aim is to make agent behaviour constrainable and provable, not merely requested in a prompt. Two distinct scopes: the coding agent that writes on my behalf, and autonomous agents once they are deployed.
這裡持續在做的事，是讓 agent 的行為變成可約束、可舉證的，而不是只用提示詞請它照做。兩個範圍不同：替我寫程式的 coding agent，以及上線後自主運行的 agent。

**Coding-agent governance ｜Coding agent 治理** — five layers, each usable on its own. 五個層面，每層都可以單獨使用。

| Layer / 層 | Repo | |
| --- | --- | --- |
| Supply chain / 供應鏈 | [SkillSpector](https://github.com/SanHsien/SkillSpector) | Scan an agent skill before installing it: static rules plus optional LLM analysis, a risk score, and a `SAFE` / `CAUTION` / `DO_NOT_INSTALL` call — runnable as a skill or as an MCP install gate ｜安裝 agent skill 前先掃描：靜態規則加可選的 LLM 分析、風險分數與安裝建議，可當 skill 或 MCP 安裝閘門 |
| Dispatch / 派工決策 | [agent-advisor](https://github.com/SanHsien/agent-advisor) | Risk-gated routing across four agent runtimes ｜四種 agent runtime 的風險分流路由 |
| Execution / 動作攔截 | [harness-guard](https://github.com/SanHsien/harness-guard) | Runtime hooks blocking dangerous commands, unevidenced completion claims, commits over failing tests ｜攔截危險指令、無證據的完成宣稱、紅燈仍提交 |
| Output / 產出品質 | [ai-quality-gates](https://github.com/SanHsien/ai-quality-gates) | Gherkin specs, coverage and mutation gates, architecture contracts, bounded agent-loop policy ｜可執行規格、覆蓋率與 mutation gate、架構契約、有界 loop policy |
| Delivery / 交付流程 | [paulsha-cortex](https://github.com/SanHsien/paulsha-cortex) | Candidate, verification, independent review, completion evidence ｜候選、驗證、獨立審查與完成證據 |

**Deployed-agent governance ｜上線 agent 治理**

| Repo | | |
| --- | --- | --- |
| [agent-governance-toolkit](https://github.com/SanHsien/agent-governance-toolkit) | Policy enforcement, zero-trust agent identity, execution sandboxing, and tamper-evident audit records for autonomous agents in production — answering what an agent is allowed to do, which agent did it, and how you prove it afterwards ｜為上線的自主 agent 提供政策強制、零信任身分、沙箱執行與可稽核記錄；回答的是「這個動作准不准」「是哪一個 agent 做的」「事後怎麼舉證」 | `Python` fork of [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) |

## Index / 專案索引

Public repositories grouped by purpose — a few highlights per row, then the full list.
公開 repo 依用途分組，每列先列幾個代表作，再連到該類完整清單。

| Category / 類別 | Selected / 精選 | |
| --- | --- | --- |
| **AI governance**<br>AI 治理 | [SkillSpector](https://github.com/SanHsien/SkillSpector) scan before install ｜安裝前掃描 · [agent-advisor](https://github.com/SanHsien/agent-advisor) risk-gated dispatch ｜風險分流派工 · [harness-guard](https://github.com/SanHsien/harness-guard) runtime hooks ｜動作攔截 | [all →](https://github.com/SanHsien?tab=repositories&q=topic%3Aai-governance&type=public) |
| **Agent skills**<br>Agent 技能包 | [agent-skills](https://github.com/SanHsien/agent-skills) spec→ship flow ｜工程流程 · [MyR2D2](https://github.com/SanHsien/MyR2D2) cross-model review ｜跨模型二審 · [book-to-skill](https://github.com/SanHsien/book-to-skill) books as skills ｜技術書轉技能 | [all →](https://github.com/SanHsien?tab=repositories&q=topic%3Aagent-skills&type=public) |
| **Agent runtime & tooling**<br>Agent runtime 與工具鏈 | [opencodex](https://github.com/SanHsien/opencodex) swap the LLM ｜換掉背後的 LLM · [agentdeck](https://github.com/SanHsien/agentdeck) tray quota cockpit ｜系統匣額度控制台 · [OpenSpec](https://github.com/SanHsien/OpenSpec) spec-driven development ｜規範驅動開發 | [all →](https://github.com/SanHsien?tab=repositories&q=topic%3Aagent-runtime&type=public) |
| **Local-first desktop**<br>本機桌面工具 | [openshelf](https://github.com/SanHsien/openshelf) export your books ｜圖書批次匯出 · [channeldepot](https://github.com/SanHsien/channeldepot) archive channels ｜頻道保存 · [voxprose](https://github.com/SanHsien/voxprose) on-device dictation ｜本機語音輸入 | [all →](https://github.com/SanHsien?tab=repositories&q=topic%3Alocal-first&type=public) |
| **Assistants & interfaces**<br>助理與介面 | [gpt-ai-assistant](https://github.com/SanHsien/gpt-ai-assistant) assistant inside LINE ｜自架 LINE 助理 · [chatgpt-sidebar](https://github.com/SanHsien/chatgpt-sidebar) browser side panel ｜瀏覽器側邊欄 · [khoj](https://github.com/SanHsien/khoj) self-hosted second brain ｜自架第二大腦 | [all →](https://github.com/SanHsien?tab=repositories&q=topic%3Aai-assistant&type=public) |
| **Content production**<br>內容產製 | [html-anything](https://github.com/SanHsien/html-anything) agent writes the HTML ｜agent 寫 HTML · [hyperframes](https://github.com/SanHsien/hyperframes) render video from HTML ｜用 HTML 渲染影片 · [video-autopilot-kit](https://github.com/SanHsien/video-autopilot-kit) video pipeline ｜影片流程自動化 | [all →](https://github.com/SanHsien?tab=repositories&q=topic%3Acontent-creation&type=public) |
| **Other**<br>其他 | [github-stars-organizer-playbook](https://github.com/SanHsien/github-stars-organizer-playbook) Stars Lists workflow ｜Stars Lists 整理 · [public-apis](https://github.com/SanHsien/public-apis) free API directory ｜免費 API 目錄 · [gpt-ai-assistant-docs](https://github.com/SanHsien/gpt-ai-assistant-docs) documentation site ｜文件站 | [all →](https://github.com/SanHsien?tab=repositories&q=topic%3Amisc&type=public) |

[Browse all public repositories ｜瀏覽全部公開 repo →](https://github.com/SanHsien?tab=repositories&q=&type=public&language=&sort=)

## How I Work / 工作方式

- **Local-first by default** ｜**預設本機優先** — if it runs on the user's machine, it does not get a hosted backend first.
  跑得動在使用者自己電腦上的東西，就不先架一個後端。
- **Release-oriented** ｜**以交付為導向** — downloadable, runnable, verifiable beats a demo.
  可下載、跑得起來、驗得出來，勝過一個 demo。
- **Privacy-aware** ｜**重視隱私邊界** — user files, images, and tokens do not go to services that do not need them.
  使用者的檔案、圖片與憑證，不送去不需要它們的服務。
- **Explicit boundaries** ｜**寫明邊界** — licensing, platform rules, unsupported cases, and operational risks are stated, not implied.
  授權、平台規則、不支援的情況與操作風險都寫出來，不靠讀者自己推測。
- **AI-assisted, still verified** ｜**AI 協作但仍要驗證** — agents do a large share of the writing; what ships still has to pass tests, packaging, and stated limits. The governance repos above exist because "the agent said it was done" is not evidence.
  程式有很大一部分是 agent 寫的；但要出貨仍得通過測試、打包與寫明的限制。上面那些治理 repo 存在的理由，就是「agent 說做完了」不算證據。

Recurring themes across the projects: local-first applications, AI in interfaces people already use, and verifiable workflows that turn repetitive work into bounded automation.
專案共通的主題：本機優先的應用程式、把 AI 放進使用者本來就在用的介面，以及把重複工作轉成有界且可驗證的自動化流程。

## Boundaries / 邊界

Private and organization-specific work stays private; this page highlights public personal projects and selected open-source maintenance work.
私人與組織專案維持不公開；本頁只展示公開的個人作品與精選的開源維護工作。

## Tools / 工具

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=111)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-306998?logo=python&logoColor=white)

## Elsewhere / 其他平台

- [LinkedIn](https://www.linkedin.com/in/sanhsien/) — professional profile / 專業檔案
- [Facebook](https://www.facebook.com/sanhsien) · [Instagram](https://www.instagram.com/sanhsien/) · [Threads](https://www.threads.com/@sanhsien) · [X](https://x.com/Hsien_3)
