# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) < 2:
        #     return len(s)
        # max_len = 0
        # simbols = []
        # for simbol in s:
        #     if simbols and simbol in simbols:
        #         max_len = max(max_len, len(simbols))
        #         simbols = simbols[simbols.index(simbol):]
        #         simbols.pop(0)
        #     simbols.append(simbol)
        # max_len = max(max_len, len(simbols))
        # return max_len

        if len(s) < 2:
            return len(s)

        simbols = {}
        left_idx, max_len = 0, 0
        for right_idx, simbol in enumerate(s):
            if simbol not in simbols:
                simbols[simbol] = right_idx
            else:
                if simbols[simbol] >= left_idx:
                    left_idx = simbols[simbol] + 1
                simbols[simbol] = right_idx

            max_len = (
                max_len
                if max_len > right_idx - left_idx + 1
                else right_idx - left_idx + 1
            )
        return max_len


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("au") == 2
    assert Solution().lengthOfLongestSubstring("abba") == 2
