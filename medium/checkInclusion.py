# https://leetcode.com/problems/permutation-in-string/


# 2025-12-28
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        a, b = {}, {}

        for i in range(len(s1)):
            a[s1[i]] = a.get(s1[i], 0) + 1
            b[s2[i]] = b.get(s2[i], 0) + 1

        for i in range(len(s1), len(s2)):
            if a == b:
                return True
            b[s2[i]] = b.get(s2[i], 0) + 1
            b[s2[i - len(s1)]] -= 1
            if b[s2[i - len(s1)]] == 0:
                del b[s2[i - len(s1)]]

        return a == b


# tests
s = Solution()
assert s.checkInclusion("ab", "eidbaooo")
assert not s.checkInclusion("ab", "eidboaoo")
assert s.checkInclusion("adc", "dcda")
assert not s.checkInclusion("hello", "ooolleoooleh")
