# https://leetcode.com/problems/longest-repeating-character-replacement/

# 2026-02-14
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = left = 0
        mostf = 0
        counts = {}

        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            mostf = max(mostf, counts[ch])

            while right - left + 1 > mostf + k:
                counts[s[left]] -= 1
                left += 1

            start = left

        return right - start + 1


# tests
s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAAA", 2) == 4
assert s.characterReplacement("ABCDE", 1) == 2
assert s.characterReplacement("BAAA", 1) == 4
assert s.characterReplacement("BAAAB", 2) == 5
