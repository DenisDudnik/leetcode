# https://leetcode.com/problems/permutation-in-string/


# 2026-02-02
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d1, d2 = {}, {}

        for i in range(len(s1)):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
            d2[s2[i]] = d2.get(s2[i], 0) + 1

        for i in range(len(s1), len(s2)):
            if d1 == d2:
                return True
            d2[s2[i]] = d2.get(s2[i], 0) + 1
            d2[s2[i - len(s1)]] -= 1
            if d2[s2[i - len(s1)]] == 0:
                del d2[s2[i - len(s1)]]

        return d1 == d2


# tests
s = Solution()
assert s.checkInclusion("ab", "eidbaooo")
assert not s.checkInclusion("ab", "eidboaoo")
assert s.checkInclusion("adc", "dcda")
assert not s.checkInclusion("hello", "ooolleoooleh")
