import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import check_profile_links as cpl  # noqa: E402


class RepoTargets(unittest.TestCase):
    def test_github_link_on_a_badge_line_is_still_checked(self):
        line = "[![stars](https://img.shields.io/github/stars/SanHsien/foo)](https://github.com/SanHsien/foo)"
        self.assertEqual(cpl.repo_targets([line]), [(1, "SanHsien", "foo")])

    def test_account_and_query_links_are_not_repos(self):
        lines = ["[x](https://github.com/SanHsien?tab=repositories&q=topic%3Amisc)"]
        self.assertEqual(cpl.repo_targets(lines), [])

    def test_path_below_repo_resolves_to_repo(self):
        lines = ["[x](https://github.com/SanHsien/foo/blob/main/a.md)"]
        self.assertEqual(cpl.repo_targets(lines), [(1, "SanHsien", "foo")])


class RelativeTargets(unittest.TestCase):
    def test_percent_encoded_name_is_decoded(self):
        self.assertEqual(cpl.relative_targets(["![](assets/my%20pic.png)"]), [(1, "assets/my pic.png")])

    def test_http_and_anchor_skipped(self):
        self.assertEqual(cpl.relative_targets(["[a](https://x.y) [b](#c)"]), [])


class Containment(unittest.TestCase):
    def test_sibling_dir_with_same_prefix_is_outside(self):
        sibling = cpl.REPO_ROOT.parent / (cpl.REPO_ROOT.name + "-evil") / "a.png"
        self.assertFalse(cpl.is_inside_repo(sibling))

    def test_file_in_repo_is_inside(self):
        self.assertTrue(cpl.is_inside_repo(cpl.REPO_ROOT / "README.md"))


if __name__ == "__main__":
    unittest.main()
