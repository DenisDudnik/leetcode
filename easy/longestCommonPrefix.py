# https://leetcode.com/problems/longest-common-prefix/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = strs[0]
        last = strs[-1]
        while not last.startswith(prefix):
            prefix = prefix[:-1]
        return prefix

                


if __name__ == "__main__":
    assert Solution().longestCommonPrefix(strs = ["flower","flow","flight"]) == "fl"
    assert Solution().longestCommonPrefix(strs = ["flower","fkow"]) == "f"
    assert Solution().longestCommonPrefix(strs = ["dog","racecar","car"]) == ""
