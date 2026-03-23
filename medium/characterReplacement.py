# https://leetcode.com/problems/longest-repeating-character-replacement/

# 2026-03-23
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = longest = 0
        most_f = 0
        ch_freqs = {}

        for right, ch in enumerate(s):
            ch_freqs[ch] = ch_freqs.get(ch, 0) + 1
            most_f = max(most_f, ch_freqs[ch])

            while right - left + 1 - most_f > k:
                ch_freqs[s[left]] -= 1
                left += 1

            if right - left + 1 > longest:
                longest = right - left + 1

        return longest


# tests
s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAAA", 2) == 4
assert s.characterReplacement("ABCDE", 1) == 2
assert s.characterReplacement("BAAA", 1) == 4
assert s.characterReplacement("BAAAB", 2) == 5
