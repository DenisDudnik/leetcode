# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    assert Solution().strStr(haystack = "sadbutsad", needle = "sad") == 0
    assert Solution().strStr(haystack = "leetcode", needle = "leeto") == -1
