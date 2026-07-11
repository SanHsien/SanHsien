# SanHsien

Local-first tools, practical automation, and AI-assisted workflows.  
本機優先工具、實用自動化，以及 AI 輔助工作流。

I build small, practical tools around local workflows, content/media processing, and AI-assisted development. This profile only lists projects that are suitable for public description; private or context-specific systems are intentionally left out.  
我主要做本機工具、自動化流程，以及和 AI 輔助工作流有關的實用專案。這裡只放適合公開的專案與描述；內部、私人或特定場域使用的系統不放在個人頁介紹。

## What I Build / 我做的方向

- **Local-first utilities**: Windows EXE, CLI tools, desktop GUI, portable workflows.  
  **本機優先工具**：Windows EXE、CLI、桌面 GUI、可攜式流程。
- **Content and media workflows**: downloading, organizing, converting, sticker making, batch processing.  
  **內容與媒體流程**：下載、整理、轉檔、貼圖製作、批次處理。
- **AI-assisted tools**: prompts, browser helpers, documentation workflows, agent-assisted development.  
  **AI 輔助工具**：提示詞、瀏覽器輔助、文件整理、agent 協作開發。
- **Documentation-first projects**: README, packaging steps, release notes, and verification records are maintained with the code.  
  **文件先行的專案**：README、打包步驟、release notes、驗證紀錄會跟著程式一起維護。

## Vibe Coding / AI 協作開發

I use AI coding agents and vibe coding to speed up prototyping, refactoring, documentation, tests, and release preparation.  
我會使用 AI coding agents 與 vibe coding 來加速雛形、重構、文件整理、測試補齊與 release 準備。

I still treat generated code as unfinished until it can be run, tested, packaged, or clearly documented with its limits.  
但我不把「AI 產生了程式」當成完成；能交付的狀態至少要能被實際執行、測試、打包，或用文件清楚交代限制。

## Public Projects / 公開專案

| Project | English | 繁體中文 | Stack |
| --- | --- | --- | --- |
| [openshelf](https://github.com/SanHsien/openshelf) | Batch export for Google Play Books: downloads DRM-free EPUB/PDF files and keeps official `.acsm` files for DRM-protected books. | 批次匯出 Google Play 圖書；無 DRM 書下載 EPUB/PDF，DRM 書保留官方 `.acsm`。 | Python, Windows EXE |
| [yt_fetch](https://github.com/SanHsien/yt_fetch) | Lightweight portable YouTube channel downloader with GUI, batch imports, cookies, and Windows portable release. | 輕巧可攜的 YouTube 頻道下載工具，支援 GUI、批次匯入、cookies 與 Windows 免安裝版本。 | Python, yt-dlp |
| [sticker-forge](https://github.com/SanHsien/sticker-forge) | Local-first chat sticker pack toolkit for LINE and multi-platform exports. | 本機優先的聊天貼圖包製作工具，支援 LINE 與多平台匯出。 | Python, pywebview, PyInstaller |
| [gpt-ai-assistant](https://github.com/SanHsien/gpt-ai-assistant) | LINE × OpenAI chatbot for chatting with a self-hosted AI assistant, image generation, image understanding, and search. Chinese docs first. | LINE × OpenAI 聊天機器人，可和自架 AI 助理聊天、生圖、看圖與搜尋；中文文件為主。 | JavaScript, LINE, OpenAI |

## How I Work / 工作方式

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
