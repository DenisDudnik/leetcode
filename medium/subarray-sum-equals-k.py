# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

# Если разница между префиксными суммами равна k, то элементы между ними (их позициями) как раз дают сумму k.
# Если текущий prefix_sum - k уже был ранее (1 и более раз), то именно столько промежутков дают сейчас сумму k
# https://www.youtube.com/watch?v=1x91vuYSibw


# 2025-12-07
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = {0: 1}
        res = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            res += prefix_dict.get(prefix_sum - k, 0)
            prefix_dict[prefix_sum] =  prefix_dict.get(prefix_sum, 0) + 1

        return res


# tests
s = Solution()
assert s.subarraySum([1, 1, 1], 2) == 2
assert s.subarraySum([1, 2, 3], 3) == 2
