# https://leetcode.com/problems/longest-repeating-character-replacement/

# 2025-12-29
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        counts = {}
        maxf = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxf = max(counts[s[right]], maxf)

            while right - left + 1 > maxf + k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


# tests
s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAAA", 2) == 4
assert s.characterReplacement("ABCDE", 1) == 2
assert s.characterReplacement("BAAA", 1) == 4
