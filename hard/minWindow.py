# https://leetcode.com/problems/minimum-window-substring/


# 2026-02-15
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(t) > len(s):
            return ""

        need = Counter(t)
        not_found = len(t)
        min_len = 10**6
        left = start = 0

        for right, ch in enumerate(s):
            if need[ch] > 0:
                not_found -= 1
            need[ch] -= 1

            while not_found == 0:
                need[s[left]] += 1
                if need[s[left]] > 0:
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
