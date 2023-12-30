# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert Solution().isAnagram(s="anagram", t="nagaram") == True
    assert Solution().isAnagram(s="rat", t="car") == False
