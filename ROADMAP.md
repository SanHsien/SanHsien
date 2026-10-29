# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-10-29 依 `main` `d0e345a649a7` 查的快照，開工前先重查 GitHub。

## 現況

GitHub profile README（public、非 fork、無 release），附兩支檢查：`tools/check_profile_links.py`（連結）與 `tools/check_index_coverage.py`（公開 repo 是否都有錨點 topic）。2026-10-29 無 open issue／PR、Dependabot 告警 0，`main` 上 CI 最近一次 success；Code scanning 未查到（API 回 404 無分析、另有權限不足訊息，不當成 0）（2026-10-29 `gh` 查詢）。每週日 23:00 UTC 的排程 CI 會因新公開 repo 缺錨點 topic 而紅，這是該檢查的預期用途，不是缺陷。

## 近期：可以直接動手
| 項目 | 為什麼 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 確認 `health-bank-toolkit` 歸在「其他（misc）」是否合意 | 深掃時暫放 `misc` 錨點；若想歸別類只需改 topic，不需改程式 | 維護者確認，或改 topic 後 `python tools/check_index_coverage.py` exit 0 | 維護者 | `gh api repos/SanHsien/health-bank-toolkit/topics`（2026-10-29 為 `misc`）；深掃報告（2026-10-26） |

## 中期：等條件成立再做
| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 為新公開 repo 補錨點 topic（或在 README 增加對應區塊） | 週日排程 CI 因 `check_index_coverage.py` 紅燈（查：`gh run list -R SanHsien/SanHsien -w CI -L 3`） | 該 repo 加上既有錨點 topic，`python tools/check_index_coverage.py` exit 0、排程 CI 轉綠；`python tools/check_profile_links.py` 與 `python -m unittest discover -s tests` 仍通過 | Claude Haiku | `.github/workflows/ci.yml:19`；`tools/check_index_coverage.py:110-121` |
| 更新 README 的作品區塊 | 維護者新增或下架代表作 | README 連結與圖片可達：`python tools/check_profile_links.py` exit 0；改動範圍由維護者決定措辭 | 維護者 | `tools/check_profile_links.py`；`README.md` |

## 刻意不做
| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 驗證 shields.io 或社群外部連結可達 | CI 設計即不驗外部站，避免噪音（接續開發報告） | 外部連結常失效並影響首頁呈現時 |
| 由 agent 改寫 README 的自我介紹與措辭 | 屬維護者的個人敘事與產品方向 | 維護者明確要求改寫某段 |
| 為了有事做而增加功能或 workflow | profile README 精簡即可，既有檢查已涵蓋連結與索引覆蓋 | 不重新考慮 |

## 維護方式

自有 repo：Dependabot 處理 Actions 升級；每週排程 CI 是「新增公開 repo 缺錨點 topic」的警報。改動以 `python -m unittest discover -s tests`、`python tools/check_profile_links.py`、`python tools/check_index_coverage.py` 為閘門。
