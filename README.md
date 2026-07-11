# SanHsien

Local-first tools, practical automation, and AI-assisted workflows.  
本機優先工具、實用自動化，以及 AI 輔助工作流。

I build small, practical tools around local workflows, content/media processing, and AI-assisted development. This profile only lists projects that are suitable for public description; private or context-specific systems are intentionally left out.

我主要做本機工具、自動化流程，以及和 AI 輔助工作流有關的實用專案。這裡只放適合公開的專案與描述；內部、私人或特定場域使用的系統不放在個人頁介紹。

## What I Build

- **Local-first utilities**: Windows EXE, CLI tools, desktop GUI, portable workflows.
- **Content and media workflows**: downloading, organizing, converting, sticker making, batch processing.
- **AI-assisted tools**: prompts, browser helpers, documentation workflows, agent-assisted development.
- **Documentation-first projects**: README, packaging steps, release notes, and verification records are maintained with the code.

## Vibe Coding

I use AI coding agents and vibe coding to speed up prototyping, refactoring, documentation, tests, and release preparation.

I still treat generated code as unfinished until it can be run, tested, packaged, or clearly documented with its limits.

我會使用 AI coding agents 與 vibe coding 來加速開發，尤其是雛形、重構、文件整理、測試補齊與 release 準備。但我不把「AI 產生了程式」當成完成；能交付的狀態至少要能被實際執行、測試、打包，或用文件清楚交代限制。

## Public Projects

| Project | What it does | Stack |
| --- | --- | --- |
| [openshelf](https://github.com/SanHsien/openshelf) | Batch export for Google Play Books: downloads DRM-free EPUB/PDF files and keeps official `.acsm` files for DRM-protected books. | Python, Windows EXE |
| [yt_fetch](https://github.com/SanHsien/yt_fetch) | Lightweight portable YouTube channel downloader with GUI, batch imports, cookies, and Windows portable release. | Python, yt-dlp |
| [sticker-forge](https://github.com/SanHsien/sticker-forge) | Local-first chat sticker pack toolkit for LINE and multi-platform exports. | Python, pywebview, PyInstaller |
| [gpt-ai-assistant](https://github.com/SanHsien/gpt-ai-assistant) | LINE × OpenAI chatbot for chatting with a self-hosted AI assistant, image generation, image understanding, and search. Chinese docs first. | JavaScript, LINE, OpenAI |

## How I Work

- **Local-first by default**: if it can run on the user's machine, I avoid starting with a hosted backend.
- **Privacy-aware**: user files, images, and tokens should not be sent to unnecessary services.
- **Release-oriented**: downloadable, runnable, and verifiable is more useful than a demo that only works once.
- **Tests and smoke checks**: important flows should have tests, real smoke checks, or clearly documented limits.
- **Clear boundaries**: licensing, platform rules, data responsibility, and unsupported use cases should be explicit.

## Tools I Use Often

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=111)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-306998?logo=python&logoColor=white)

## Notes

- Most public projects start with a Traditional Chinese README. Public-facing tools may also include English docs, packaging notes, and release files.
- Private or internal-use projects are not listed here, even if they exist on GitHub.
