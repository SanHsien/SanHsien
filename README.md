# SanHsien

Local-first tools, practical automation, and small systems that solve real workflows.

我主要做本機工具、校務／行政系統、自動化流程，以及和 AI 輔助工作流有關的實用專案。專案通常重視可下載、可驗證、可維護，不把使用者資料送到不必要的服務。

## 目前重點

- **本機優先工具**：Windows EXE、CLI、桌面 GUI、離線或低依賴流程。
- **行政與教育場景**：表單、審核、匯出、權限、Excel / MySQL / LDAP 整合。
- **AI 輔助工作流**：提示詞、文件整理、瀏覽器工具、個人知識與記憶備份。
- **清楚的邊界**：不碰不該碰的資料、不代管不必要的 API key、不模糊授權與責任。

## 代表專案

| 專案 | 內容 | 技術 |
| --- | --- | --- |
| [openshelf](https://github.com/SanHsien/openshelf) | 批次匯出 Google Play 圖書；無 DRM 書下載 EPUB/PDF，DRM 書保留官方 `.acsm`。 | Python, Windows EXE |
| [yt_fetch](https://github.com/SanHsien/yt_fetch) | 輕巧可攜的 YouTube 頻道下載工具，支援 GUI、批次匯入、cookies 與 Windows 免安裝。 | Python, yt-dlp, GUI |
| [sticker-forge](https://github.com/SanHsien/sticker-forge) | 本機優先的聊天貼圖包製作工具，支援 LINE 與多平台匯出。 | Python, pywebview, PyInstaller |
| [student-achievement-upload-system](https://github.com/SanHsien/student-achievement-upload-system) | 學生證照與競賽成果上傳系統，含後台查詢與 Excel 匯出。 | PHP, Slim, MySQL, LDAP |
| [key-checkout-system](https://github.com/SanHsien/key-checkout-system) | 教室鑰匙借用、歸還、預借與查詢系統。 | Excel VBA |
| [chatgpt-sidebar](https://github.com/SanHsien/chatgpt-sidebar) | Chrome 側邊欄摘要工具，針對目前頁面產生中文摘要。 | JavaScript, Chrome Extension |

## 常用技術

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=111)
![VBA](https://img.shields.io/badge/VBA-217346?logo=microsoft-excel&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)

## 做專案時在意的事

- **能交付**：README、打包流程、測試與 release 要能讓使用者真的跑起來。
- **能驗證**：重要功能要有測試或實機 smoke test，不只靠靜態檢查。
- **能維護**：文件跟程式一起更新，路線圖不留過期承諾。
- **尊重邊界**：授權、資料隱私、平台規範與使用者責任要寫清楚。

## GitHub

我的公開 repo 以實用工具與工作流系統為主。多數專案會附上繁體中文 README；如果專案適合公開使用，也會補英文 README、打包說明與 release 檔案。
