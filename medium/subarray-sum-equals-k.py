# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

# Если разница между префиксными суммами равна k, то элементы между ними (их позициями) как раз дают сумму k.
# Если текущий prefix_sum - k уже был ранее (1 и более раз), то именно столько промежутков дают сейчас сумму k
# https://www.youtube.com/watch?v=1x91vuYSibw


# 2025-12-16
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_dict = {0: 1}
        pre_sum = 0
        result = 0

        for n in nums:
            pre_sum += n
            result += pre_dict.get(pre_sum - k, 0)
            pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1

        return result


# tests
s = Solution()
assert s.subarraySum([1, 1, 1], 2) == 2
assert s.subarraySum([1, 2, 3], 3) == 2
