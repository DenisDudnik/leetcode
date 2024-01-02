# https://leetcode.com/problems/group-anagrams/


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for str_ in strs:
            d["".join(sorted(str_))].append(str_)

        return list(d.values())


if __name__ == "__main__":
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]
