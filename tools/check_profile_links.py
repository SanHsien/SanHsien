#!/usr/bin/env python3
"""驗證 profile README 指向的東西還在。

為什麼是這個檢查，不是一般的連結檢查
------------------------------------
這個 repo 沒有程式碼、沒有套件 manifest、沒有可執行的東西，所以照搬艦隊的
`check_links.py`（只驗相對連結）會得到一支什麼都沒驗的裝飾 workflow——`AGENTS.md`
明講不要那種東西。但這個 README **有**一種會安靜壞掉的東西：它是對外的門面，
列了十幾個指向本帳號 repo 的連結，而 repo 會被改名、轉私有、封存。發生的時候
profile 首頁就是一排 404，而沒有任何人會收到通知。

所以這裡驗兩件事，兩件都是決定性的、不靠外部網站的心情：

1. **相對路徑真的存在**（banner 圖）。檔案改名或搬走，README 就破圖。
2. **每個 `github.com/<owner>/<repo>` 連結在 GitHub API 上查得到、而且沒有被改名**。
   查的是 API 不是抓網頁，所以不會有 rate-limit 之外的偽陽性；改名會被 API 的
   `full_name` 抓出來（GitHub 會自動轉址，人眼看不出來，但連結已經指到舊名字）。

**刻意不驗**的東西：`img.shields.io` 的 badge、社群平台個人頁、Chrome Web Store、
GitHub Pages 文件站。那些是第三方服務，會因為限流、地區、反爬蟲而間歇性紅燈，
把它們放進必要檢查只會訓練出「紅了就重跑」的習慣，那比不檢查更糟。

用法
----
    python tools/check_profile_links.py            # 需要 GITHUB_TOKEN 才查得順（未帶也能跑，會受匿名限流）

有任何一項失敗就 exit 1，並印出是哪一行、哪一個連結、為什麼。
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"

# `![](path)`、`[text](path)` 與 HTML 的 src="path"。只收相對路徑，http(s) 與錨點跳過。
RELATIVE_MD = re.compile(r"\]\((?!https?:|#|mailto:)([^)\s]+)\)")
RELATIVE_HTML = re.compile(r"""(?:src|href)\s*=\s*["'](?!https?:|#|mailto:)([^"']+)["']""")

# github.com/<owner>/<repo>，排除 github.com/<owner> 這種只有帳號的、以及帶 query 的清單頁。
REPO_URL = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?=[)\s\"'/]|$)")

# 第三方服務：刻意不驗，理由見模組說明。
SKIP_HOSTS = ("img.shields.io", "chromewebstore.google.com")


def read_readme() -> list[str]:
    if not README.is_file():
        raise SystemExit(f"找不到 {README}——這個檢查的對象不見了，先確認檔案還在。")
    return README.read_text(encoding="utf-8").splitlines()


def relative_targets(lines: list[str]) -> list[tuple[int, str]]:
    found: list[tuple[int, str]] = []
    for number, line in enumerate(lines, start=1):
        for pattern in (RELATIVE_MD, RELATIVE_HTML):
            for match in pattern.finditer(line):
                target = match.group(1).split("#", 1)[0].strip()
                if target:
                    found.append((number, target))
    return found


def repo_targets(lines: list[str]) -> list[tuple[int, str, str]]:
    found: list[tuple[int, str, str]] = []
    for number, line in enumerate(lines, start=1):
        if any(host in line for host in SKIP_HOSTS):
            continue
        for match in REPO_URL.finditer(line):
            owner, repo = match.group(1), match.group(2).removesuffix(".git")
            if repo.startswith("?"):
                continue
            found.append((number, owner, repo))
    return found


def fetch_repo(owner: str, repo: str) -> tuple[int, dict]:
    """回傳 (HTTP 狀態, 內容)。網路層錯誤讓它往上拋，不要假裝成 404。"""
    request = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "sanhsien-profile-link-check",
        },
    )
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        return error.code, {}


def main() -> int:
    lines = read_readme()
    failures: list[str] = []

    relatives = relative_targets(lines)
    for number, target in relatives:
        path = (REPO_ROOT / target).resolve()
        if not str(path).startswith(str(REPO_ROOT)):
            failures.append(f"README.md:{number} 相對路徑跑出 repo 之外：{target}")
        elif not path.exists():
            failures.append(f"README.md:{number} 相對路徑不存在：{target}")

    repos = repo_targets(lines)
    seen: dict[tuple[str, str], None] = {}
    for number, owner, repo in repos:
        key = (owner.lower(), repo.lower())
        if key in seen:
            continue
        seen[key] = None
        status, payload = fetch_repo(owner, repo)
        if status == 404:
            failures.append(f"README.md:{number} repo 查不到（已刪除、轉私有或改名）：{owner}/{repo}")
        elif status == 403:
            failures.append(
                f"README.md:{number} GitHub API 回 403（多半是匿名限流）：{owner}/{repo}"
                "——這是檢查本身跑不完，不是連結壞掉；在 CI 帶 GITHUB_TOKEN 再跑一次。"
            )
        elif status != 200:
            failures.append(f"README.md:{number} GitHub API 回 {status}：{owner}/{repo}")
        else:
            actual = payload.get("full_name", "")
            if actual and actual.lower() != f"{owner}/{repo}".lower():
                failures.append(
                    f"README.md:{number} repo 已改名：連結寫 {owner}/{repo}，實際是 {actual}"
                    "（GitHub 會自動轉址，所以人眼看不出來）"
                )

    print(f"相對路徑 {len(relatives)} 條、GitHub repo 連結 {len(seen)} 個（去重後）")
    if failures:
        print()
        for line in failures:
            print(f"  ✗ {line}")
        print(f"\n{len(failures)} 項未通過。")
        return 1
    print("全部通過。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
