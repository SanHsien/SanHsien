#!/usr/bin/env python3
"""確認每個公開 repo 都被 README 索引的某一類涵蓋。

為什麼需要這個檢查
------------------
README 的 `## Index / 專案索引` 每一類都有一個**錨點 topic**，那一列的「all →」連到
`?tab=repositories&q=topic:<錨點>`。這個設計的好處是新 repo 不必改 README；代價是
**新 repo 如果沒打上任何錨點 topic，就從索引裡整個消失**——而且不會有任何徵兆：
README 沒壞、連結沒壞、CI 全綠，只是那個 repo 沒人找得到。

`check_profile_links.py` 抓不到這種失效，因為它驗的是「README 指到的東西還在嗎」，
而這裡的問題是「存在的東西 README 指不到」——方向相反。所以要分成兩支。

刻意不驗的事
------------
不驗「錨點 topic 在 README 裡真的有對應的一列」。那需要解析 markdown 表格，而表格
格式是人在改的，解析器會比它要保護的東西還脆弱。ANCHORS 與 README 對齊靠的是改動時
一起改，不是靠機器；這支只回答「有沒有 repo 掉出去」。

私有 repo 不算，因為索引只列公開的。

用法
----
    python tools/check_index_coverage.py          # 需要 GITHUB_TOKEN，否則受匿名限流

有 repo 沒被涵蓋就 exit 1，並印出可直接執行的補 topic 指令。
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

# Windows 主控台預設 cp950，編碼不了 ✗（U+2717）會直接 UnicodeEncodeError——
# 而那只在「有 repo 掉出去」時才走到，也就是最需要看到輸出的時候整支崩掉。
# CI 跑在 UTF-8 的 Linux 上，所以這個 bug 在 CI 永遠不會現形。
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OWNER = "SanHsien"

# README 索引每一類的錨點 topic。改索引分類時，這裡要一起改。
ANCHORS = (
    "ai-governance",
    "agent-skills",
    "agent-runtime",
    "local-first",
    "ai-assistant",
    "content-creation",
    "misc",  # 索引的「其他」那一列；不屬於上面任何主題但仍該被找得到的東西
)

# 不屬於任何作品分類、刻意不放進索引的 repo。
# 放進來要寫理由——這個清單是豁免，不是垃圾桶。
#
# 「其他」有了 `misc` 錨點之後，這裡只剩下真正不是作品的那一個。先前
# gpt-ai-assistant-docs／public-apis／github-stars-organizer-playbook 被列為豁免，
# 其實是因為「其他」那一列沒有錨點——用豁免去補分類設計的洞，洞補好就不需要豁免了。
EXEMPT = {
    "SanHsien": "profile README 本身，不是作品",
}


def api(path: str) -> list | dict:
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "sanhsien-profile-index-coverage",
        },
    )
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        if error.code == 403:
            raise SystemExit(
                "GitHub API 回 403（多半是匿名限流）——這是檢查跑不完，不是真的有 repo 掉出去。"
                "帶 GITHUB_TOKEN 再跑一次。"
            ) from error
        raise SystemExit(f"GitHub API 回 {error.code}：{path}") from error


def public_repos() -> list[dict]:
    """列出公開、未封存的 repo。封存的不必分類，它們已經不動了。"""
    found: list[dict] = []
    page = 1
    while True:
        batch = api(f"/users/{OWNER}/repos?type=owner&per_page=100&page={page}")
        if not batch:
            break
        found.extend(r for r in batch if not r.get("private") and not r.get("archived"))
        if len(batch) < 100:
            break
        page += 1
    return found


def main() -> int:
    repos = public_repos()
    uncovered: list[str] = []
    for repo in repos:
        name = repo["name"]
        if name in EXEMPT:
            continue
        if not (set(repo.get("topics") or []) & set(ANCHORS)):
            uncovered.append(name)

    covered = len(repos) - len(uncovered) - sum(1 for r in repos if r["name"] in EXEMPT)
    print(f"公開 repo {len(repos)} 個：{covered} 個有錨點 topic、"
          f"{sum(1 for r in repos if r['name'] in EXEMPT)} 個豁免、{len(uncovered)} 個未涵蓋")

    if not uncovered:
        print("全部通過。")
        return 0

    print("\n以下 repo 沒有任何錨點 topic，不會出現在 README 索引的任何一類：\n")
    for name in sorted(uncovered):
        print(f"  ✗ {name}")
    print(f"\n錨點 topic：{'、'.join(ANCHORS)}")
    print("\n補上分類（把 <錨點> 換成該 repo 所屬的那一個，其餘既有 topic 會保留）：\n")
    for name in sorted(uncovered):
        print(f"  gh api repos/{OWNER}/{name}/topics -X PUT --input - <<< "
              f'\'{{"names": [<既有 topic>, "<錨點>"]}}\'')
    print("\n若這個 repo 本來就不該進索引，把它加進本檔的 EXEMPT 並寫下理由。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
