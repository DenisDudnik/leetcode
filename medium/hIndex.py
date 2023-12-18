# https://leetcode.com/problems/h-index/

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for idx in range(len(citations)):
            if citations[idx]<idx+1:
                return idx
        return len(citations)


if __name__ == "__main__":
    assert Solution().hIndex([3,0,6,1,5]) == 3
    assert Solution().hIndex([1,3,1]) == 1
    assert Solution().hIndex([3,3,3]) == 3
