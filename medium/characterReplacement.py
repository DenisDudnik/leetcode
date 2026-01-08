# https://leetcode.com/problems/longest-repeating-character-replacement/

# 2026-01-07
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        s_dict = {}
        left = 0
        most_f = 0

        for right, ch in enumerate(s):
            s_dict[ch] = s_dict.get(ch, 0) + 1
            most_f = max(most_f, s_dict[ch])
            while right - left + 1 > most_f + k:
                s_dict[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


# tests
s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAAA", 2) == 4
assert s.characterReplacement("ABCDE", 1) == 2
assert s.characterReplacement("BAAA", 1) == 4
assert s.characterReplacement("BAAAB", 2) == 5
