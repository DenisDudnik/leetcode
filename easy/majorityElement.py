# https://leetcode.com/problems/majority-element/

from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
            
        


if __name__ == "__main__":
    assert Solution().majorityElement([3,2,3]) == 3
    assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2
