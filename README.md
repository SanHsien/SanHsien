# SanHsien

I build practical Windows-first tools, workflow automations, and self-hosted AI assistants, mostly with Python, JavaScript, and AI-assisted development.<br>
我主要製作實用的 Windows 優先工具、工作流自動化與自架 AI 助理，常用 Python、JavaScript 與 AI 協作開發。

Practical delivery matters to me: runnable tools, clear README files, packaging steps, release notes, and verification records.  
我重視實際交付：能執行的工具、清楚的 README、打包步驟、release notes 與驗證紀錄。

## Focus / 方向

- **Local-first tools / 本機優先工具**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Windows EXE, CLI, desktop GUI, portable workflows.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Windows EXE、CLI、桌面 GUI、可攜式流程。

- **Content and media workflows / 內容與媒體流程**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Downloading, organizing, transcoding, sticker making, batch processing.<br>
&nbsp;&nbsp;&nbsp;&nbsp;下載、整理、轉檔、貼圖製作、批次處理。

- **Accessible AI / 容易使用的 AI**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Putting AI into familiar interfaces like LINE, lowering the barrier for family to use new tools.<br>
&nbsp;&nbsp;&nbsp;&nbsp;把 AI 放進 LINE 等熟悉介面，減少家人使用新工具的門檻。

- **AI-assisted development / AI 協作開發**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Prompting, docs organizing, agent collaboration, vibe coding with verification.<br>
&nbsp;&nbsp;&nbsp;&nbsp;prompt、文件整理、agent 協作、有驗證的 vibe coding。

Current emphasis: approachable tools and assistants that can be run, checked, and maintained without unnecessary dependencies.<br>
目前重點：容易上手、可執行、可驗證、可維護，且不增加不必要依賴的工具與助理。

## Public Projects / 公開專案

### [agentdeck](https://github.com/SanHsien/agentdeck)

Windows-first system tray cockpit for Claude Code, Codex, and Antigravity: local quota monitoring, multi-model roundtable discussions, subagent role deployment, and HTML reports. Derived from `usage` and independently maintained for Windows; reads local files only and never calls usage APIs.

Windows 優先的 Claude Code、Codex 與 Antigravity 系統匣控制台：本機額度監看、多模型圓桌討論、subagent 角色部署與 HTML 報告。衍生自 `usage`，針對 Windows 獨立維護；只讀取本機檔案，不呼叫用量 API。

`Python` `Windows` `System tray` `Local-first` `Independent fork`

### [gpt-ai-assistant](https://github.com/SanHsien/gpt-ai-assistant)

Self-hosted LINE × OpenAI personal assistant that brings chat, voice, vision, image generation, sourced search, weather, Google Calendar/Tasks, and durable reminders into a familiar LINE conversation. Independently maintained and verified with real LINE/Supabase/Google acceptance, with its own [docs site](https://sanhsien.github.io/gpt-ai-assistant-docs/), CI, and tagged releases.

自架的 LINE × OpenAI 個人助理，把聊天、語音、看圖、生圖、附來源搜尋、天氣、Google Calendar／Tasks 與可靠提醒放進熟悉的 LINE 對話。準備 API 額度即可替自己或家人建立 AI 入口，不必先學新的 AI App。專案已獨立維護並完成真實 LINE／Supabase／Google 驗收，附獨立[文件站](https://sanhsien.github.io/gpt-ai-assistant-docs/)、CI 與版本 release。

`JavaScript` `LINE` `OpenAI` `Supabase` `Google Calendar` `Independent`

### [voxprose](https://github.com/SanHsien/voxprose)

聲成文 VoxProse — local-first AI voice typing for Windows: global-hotkey recording, on-device Faster-Whisper recognition (CUDA-accelerated), optional LLM polishing and translation, typed straight into the focused window. Derived from VoiceType4TW, independently maintained with 450+ tests, CI, and verified portable releases.

聲成文 VoxProse——Windows 本機優先 AI 語音輸入工具：全域快捷鍵錄音、本地 Faster-Whisper 辨識（支援 CUDA 加速）、可選 LLM 潤飾與翻譯，文字直接打進目前視窗。衍生自 VoiceType4TW、獨立維護，附 450+ 測試、CI 與可驗證的可攜版 release。

`Python` `PyQt6` `Faster-Whisper` `Active` `Windows release`

### [voxavatar](https://github.com/SanHsien/voxavatar)

Windows-only, local-first VRM desktop companion that turns an AI assistant's playback into visible lip-sync, motions, character states, and comic-style message bubbles. Codex and compatible agents can control it through a loopback-only MCP server. Derived from `xikhar/persona` and independently maintained as VoxAvatar, with CI, security gates, and Windows releases.

Windows-only、本機優先的 VRM 桌面角色陪伴：把 AI 助理的播放聲音呈現為口型、動作、角色狀態與漫畫式訊息氣泡，並讓 Codex 等相容代理透過僅限本機的 MCP 控制。衍生自 `xikhar/persona`，現以 VoxAvatar 獨立維護，附 CI、安全閘門與 Windows release。

`TypeScript` `Electron` `VRM / VRMA` `MCP` `Local-first` `Windows release`

## Private & Earlier Work / 非公開與早期作品

Some projects were built for private, organizational, or earlier professional contexts. I describe the problems and delivered capabilities without naming employers, clients, organizations, repositories, production systems, accounts, or real data.<br>
部分作品來自私人、組織內部或早期工作情境。以下說明解決的問題與交付能力，但不公開任職公司、客戶／學校／組織、repo、正式環境、帳號或真實資料。

- **Business operations automation / 營運流程自動化**<br>
  Excel VBA tools for inventory, purchasing and sales records, recurring reports, data checks, and maintainable office workflows.<br>
  使用 Excel VBA 製作進銷存、採購與銷售紀錄、定期報表、資料檢核及可交接維護的辦公流程。
- **Field and mobile workflows / 外勤與行動流程**<br>
  Earlier Palm and Android phone/tablet apps for visit records, sales activity, form entry, and online result submission.<br>
  早期曾製作 Palm 與 Android 手機／平板程式，處理拜訪紀錄、銷售活動、表單輸入與連網成果回傳。
- **Internal information systems / 內部資訊系統**<br>
  - **Web-based submission and review / 線上填報與審查**<br>
    Directory-account sign-in; certificate, language qualification, and competition submissions; linked validation, evidence uploads, automatic classification, admin review/search, and detailed or summary Excel exports—replacing paper forms and repeated spreadsheet entry.<br>
    組織帳號登入；證照、外語與競賽成果填報；聯動驗證、附件上傳、自動分類、後台審閱／查詢及 Excel 明細／統計匯出，取代紙本與重複試算表登錄。<br>
    `PHP` `MySQL / MariaDB` `LDAP / Active Directory` `Bootstrap` `DataTables`
  - **Excel/VBA key checkout and reservation / Excel/VBA 鑰匙借還與預借**<br>
    Borrower identification; checkout/return and key status; reservations and schedule lookup; overdue reminders, dashboards, history, reports, exports, roster sync, backups, and archives—turning manual logs into a maintainable operational workflow.<br>
    借用者識別、借還與鑰匙狀態、預借與課表查詢、逾時提醒、儀表板、歷史查詢、報表匯出、名單同步、備份與封存，將人工紀錄整理成可維護的作業流程。<br>
    `Excel VBA` `UserForms` `PowerShell` `Windows`
  - Tests, migration/rollback or backup checks, data dictionaries, operating guides, and handover documents support ongoing maintenance.<br>
    兩套系統均補有測試、遷移／回復或備份檢查、資料字典、操作手冊與交接文件，確保可持續維護。

## How I Work / 工作方式

- **Vibe coding with verification / 有驗證的 vibe coding**<br>
&nbsp;&nbsp;&nbsp;&nbsp;AI coding agents help with prototyping, refactoring, docs, tests, and release prep; generated code still needs to run or have its limits documented.<br>
&nbsp;&nbsp;&nbsp;&nbsp;AI coding agent 協助原型、重構、文件、測試與發版準備；產生的程式碼仍須實際執行，或把限制寫清楚。

- **Local-first by default / 預設本機優先**<br>
&nbsp;&nbsp;&nbsp;&nbsp;If it can run on the user's machine, I avoid starting with a hosted backend.<br>
&nbsp;&nbsp;&nbsp;&nbsp;能在使用者本機執行的，就不從雲端後端開始。

- **Privacy-aware / 重視隱私邊界**<br>
&nbsp;&nbsp;&nbsp;&nbsp;User files, images, and tokens should not be sent to unnecessary services.<br>
&nbsp;&nbsp;&nbsp;&nbsp;使用者的檔案、圖片與 token 不送往不必要的服務。

- **Release-oriented / 以交付為導向**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Downloadable, runnable, and verifiable beats a one-off demo.<br>
&nbsp;&nbsp;&nbsp;&nbsp;可下載、可執行、可驗證，勝過一次性 demo。

- **Clear boundaries / 清楚寫明邊界**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Licensing, platform rules, data responsibility, and unsupported use cases should be explicit.<br>
&nbsp;&nbsp;&nbsp;&nbsp;授權、平台規則、資料責任與不支援的使用情境都應明確寫出。

## Tools / 工具

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=111)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-306998?logo=python&logoColor=white)

## Notes / 備註

- Traditional Chinese first; English when useful for public-facing tools.  
  繁體中文優先；適合公開使用的工具會補英文說明。
- Private or internal-use work is summarized by capability and outcome; identifying or sensitive details are omitted.<br>
  私人或內部用途的作品只摘要能力與成果，不公開可識別或敏感資訊。
