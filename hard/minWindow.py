# https://leetcode.com/problems/minimum-window-substring/


# 2026-04-09
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        from collections import Counter

        t_counter = Counter(t)
        not_found = len(t)
        start = left = 0
        min_len = 10**6

        for right, ch in enumerate(s):
            t_counter[ch] -= 1
            if t_counter[ch] >= 0:
                not_found -= 1
            while not_found == 0:
                t_counter[s[left]] += 1
                if t_counter[s[left]] > 0:
                    not_found += 1
                if right - left + 1 <= min_len:
                    start = left
                    min_len = right - left + 1
                left += 1

        return "" if min_len == 10**6 else s[start : start + min_len + 1]


if __name__ == "__main__":
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="a", t="a") == "a"
    assert Solution().minWindow(s="a", t="aa") == ""
