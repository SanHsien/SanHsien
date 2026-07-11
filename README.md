# SanHsien

Local-first tools, practical automation, and AI-assisted workflows.

我主要做本機工具、自動化流程，以及和 AI 輔助工作流有關的實用專案。這裡只放適合公開的專案與描述；內部、私人或特定場域使用的系統不放在個人頁介紹。

## What I Build

- **Local-first utilities**：Windows EXE、CLI、桌面 GUI、portable tools。
- **Content and media workflows**：下載、整理、轉檔、貼圖製作、批次處理。
- **AI-assisted tools**：prompt、瀏覽器輔助、文件整理、agent 工作流。
- **Documentation-first projects**：README、打包步驟、release notes、驗證紀錄會跟著程式一起維護。

## Vibe Coding

我會使用 AI coding agents 與 vibe coding 來加速開發，尤其是雛形、重構、文件整理、測試補齊與 release 準備。

但我不把「AI 產生了程式」當成完成。能交付的狀態至少要能被實際執行、測試、打包或用文件清楚交代限制。

## Public Projects

| Project | What it does | Stack |
| --- | --- | --- |
| [openshelf](https://github.com/SanHsien/openshelf) | 批次匯出 Google Play 圖書；無 DRM 書下載 EPUB/PDF，DRM 書保留官方 `.acsm`。 | Python, Windows EXE |
| [yt_fetch](https://github.com/SanHsien/yt_fetch) | 輕巧可攜的 YouTube 頻道下載工具，支援 GUI、批次匯入、cookies 與 Windows 免安裝。 | Python, yt-dlp |
| [sticker-forge](https://github.com/SanHsien/sticker-forge) | 本機優先的聊天貼圖包製作工具，支援 LINE 與多平台匯出。 | Python, pywebview, PyInstaller |
| [chatgpt-sidebar](https://github.com/SanHsien/chatgpt-sidebar) | Chrome 側邊欄摘要工具，針對目前頁面產生中文摘要。 | JavaScript, Chrome Extension |

## How I Work

- **Local-first by default**：能在使用者電腦處理，就不先做 hosted backend。
- **Privacy-aware**：不把使用者檔案、圖片或 token 送到不必要的服務。
- **Release-oriented**：可下載、可執行、可驗證，比只停在 demo 更重要。
- **Tests and smoke checks**：重要流程要能跑測試、實機 smoke 或明確列出限制。
- **Clear boundaries**：授權、平台規範、資料責任與不支援範圍要寫清楚。

## Tools I Use Often

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=111)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-306998?logo=python&logoColor=white)
![Chrome Extensions](https://img.shields.io/badge/Chrome_Extensions-4285F4?logo=googlechrome&logoColor=white)

## Notes

- 多數公開專案以繁體中文 README 為主；適合公開使用的工具會補英文 README、打包說明與 release 檔案。
- 私人或內部用途的專案即使在 GitHub 上存在，也不會放在這個個人頁當代表專案。
