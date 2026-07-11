# SanHsien

I build small Windows-first tools and workflow automations, mostly with Python, JavaScript, and AI-assisted development.  
我主要製作 Windows 優先的小工具與工作流自動化，常用 Python、JavaScript 與 AI 協作開發。

The common thread across my projects is practical delivery: runnable tools, clear README files, packaging steps, release notes, and verification records.  
我的專案重點是實際交付：能執行的工具、清楚的 README、打包步驟、release notes 與驗證紀錄。

Traditional Chinese first; English when useful for public-facing tools.  
繁體中文優先；適合公開使用的工具會補英文說明。

## What I Build / 我做的方向

- **Local-first utilities**: Windows EXE, CLI tools, desktop GUI, portable workflows.  
  **本機優先工具**：Windows EXE、CLI、桌面 GUI、可攜式流程。
- **Content and media workflows**: downloading, organizing, converting, sticker making, batch processing.  
  **內容與媒體流程**：下載、整理、轉檔、貼圖製作、批次處理。
- **AI-assisted tools**: prompts, browser helpers, documentation workflows, agent-assisted development.  
  **AI 輔助工具**：提示詞、瀏覽器輔助、文件整理、agent 協作開發。
- **Documentation-first projects**: README, packaging steps, release notes, and verification records maintained with the code.  
  **文件先行的專案**：README、打包步驟、release notes、驗證紀錄會跟著程式一起維護。

## Public Projects / 公開專案

| Project | English | 繁體中文 | Stack | Status |
| --- | --- | --- | --- | --- |
| [openshelf](https://github.com/SanHsien/openshelf) | Batch export for Google Play Books: downloads DRM-free EPUB/PDF files and keeps official `.acsm` files for DRM-protected books. | 批次匯出 Google Play 圖書；無 DRM 書下載 EPUB/PDF，DRM 書保留官方 `.acsm`。 | Python, Windows EXE | Active, Windows release |
| [yt_fetch](https://github.com/SanHsien/yt_fetch) | Lightweight portable YouTube channel downloader with GUI, batch imports, cookies, and Windows portable release. | 輕巧可攜的 YouTube 頻道下載工具，支援 GUI、批次匯入、cookies 與 Windows 免安裝版本。 | Python, yt-dlp | Active, Windows release |
| [sticker-forge](https://github.com/SanHsien/sticker-forge) | Local-first chat sticker pack toolkit for LINE and multi-platform exports. | 本機優先的聊天貼圖包製作工具，支援 LINE 與多平台匯出。 | Python, pywebview, PyInstaller | Active, local-first |
| [gpt-ai-assistant](https://github.com/SanHsien/gpt-ai-assistant) | LINE × OpenAI chatbot for chatting with a self-hosted AI assistant, image generation, image understanding, and search. Chinese docs first. | LINE × OpenAI 聊天機器人，可和自架 AI 助理聊天、生圖、看圖與搜尋；中文文件為主。 | JavaScript, LINE, OpenAI | Public fork, customized docs |

## Private Work / 非公開工作

Some work is private or context-specific, so I summarize only the general shape: internal workflow tools, data collection systems, office automation, and maintenance handover documents.  
部分工作屬於私人或特定場域用途，因此只概略描述能力範圍：內部流程工具、資料收集系統、辦公自動化，以及維護交接文件。

## How I Work / 工作方式

- **Vibe coding with verification**: I use AI coding agents for prototyping, refactoring, documentation, tests, and release prep, but generated code is not done until it can run or its limits are documented.  
  **有驗證的 vibe coding**：我會用 AI coding agents 加速雛形、重構、文件、測試與 release 準備，但 AI 產生的程式不等於完成，必須能執行或清楚交代限制。
- **Local-first by default**: if it can run on the user's machine, I avoid starting with a hosted backend.  
  **預設本機優先**：能在使用者電腦處理，就不先做 hosted backend。
- **Privacy-aware**: user files, images, and tokens should not be sent to unnecessary services.  
  **重視隱私邊界**：使用者檔案、圖片與 token 不送到不必要的服務。
- **Release-oriented**: downloadable, runnable, and verifiable is more useful than a demo that only works once.  
  **以交付為導向**：可下載、可執行、可驗證，比只跑一次的 demo 更重要。
- **Tests and smoke checks**: important flows should have tests, real smoke checks, or clearly documented limits.  
  **測試與 smoke check**：重要流程要有測試、實機 smoke，或明確列出限制。
- **Clear boundaries**: licensing, platform rules, data responsibility, and unsupported use cases should be explicit.  
  **清楚寫明邊界**：授權、平台規範、資料責任與不支援範圍要講清楚。

## Tools I Use Often / 常用工具

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=111)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-306998?logo=python&logoColor=white)

## Notes / 備註

- Most public projects start with a Traditional Chinese README. Public-facing tools may also include English docs, packaging notes, and release files.  
  多數公開專案以繁體中文 README 為主；適合公開使用的工具會補英文文件、打包說明與 release 檔案。
- Private or internal-use projects are not listed here, even if they exist on GitHub.  
  私人或內部用途的專案即使在 GitHub 上存在，也不會放在這個個人頁當代表專案。
