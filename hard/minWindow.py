# https://leetcode.com/problems/minimum-window-substring/


# 2026-01-09
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        from collections import Counter

        t_count = Counter(t)
        missing = len(t)

        left = start = 0
        min_len = 2 * 10**5

        for right, ch in enumerate(s):
            if t_count[ch] > 0:
                missing -= 1
            t_count[ch] -= 1

            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                t_count[s[left]] += 1
                if t_count[s[left]] > 0:
                    missing += 1
                left += 1


        return "" if min_len == 2 * 10**5 else s[start : start + min_len]


if __name__ == "__main__":
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="a", t="a") == "a"
    assert Solution().minWindow(s="a", t="aa") == ""
