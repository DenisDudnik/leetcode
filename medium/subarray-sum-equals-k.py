# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

# Если разница между префиксными суммами равна k, то элементы между ними (их позициями) как раз дают сумму k.
# Если текущий prefix_sum - k уже был ранее (1 и более раз), то именно столько промежутков дают сейчас сумму k
# https://www.youtube.com/watch?v=1x91vuYSibw


# 2025-12-18
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_dict = {0: 1}
        result = 0
        s = 0

        for num in nums:
            s += num
            result += nums_dict.get(s - k, 0)
            nums_dict[s] = nums_dict.get(s, 0) + 1

        return result


# tests
s = Solution()
assert s.subarraySum([1, 1, 1], 2) == 2
assert s.subarraySum([1, 2, 3], 3) == 2
