# https://leetcode.com/problems/minimum-window-substring/


# 2026-01-16
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(s) < len(t):
            return ""

        need = Counter(t)
        not_found = len(t)
        left = start = 0
        size = float("inf")

        for right, ch in enumerate(s):
            if need[ch] > 0:
                not_found -= 1
            need[ch] -= 1

            while not_found == 0:
                if right - left + 1 < size:
                    start = left
                    size = right - left + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    not_found += 1
                left += 1

        return "" if size == float("inf") else s[start : start + size]


if __name__ == "__main__":
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="a", t="a") == "a"
    assert Solution().minWindow(s="a", t="aa") == ""
