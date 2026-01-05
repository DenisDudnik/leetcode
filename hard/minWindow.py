# https://leetcode.com/problems/minimum-window-substring/


# 2026-01-05
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)

        left = start = 0
        min_len = 10**6

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if right - left + 1 <= min_len:
                    start = left
                    min_len = right - left + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if min_len == 10**6 else s[start : start + min_len]


if __name__ == "__main__":
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="a", t="a") == "a"
    assert Solution().minWindow(s="a", t="aa") == ""
