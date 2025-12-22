# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

# Если разница между префиксными суммами равна k, то элементы между ними (их позициями) как раз дают сумму k.
# Если текущий prefix_sum - k уже был ранее (1 и более раз), то именно столько промежутков дают сейчас сумму k
# https://www.youtube.com/watch?v=1x91vuYSibw


# 2025-12-18
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sums = {0: 1}
        s = 0

        for n in nums:
            s += n
            result += prefix_sums.get(s - k, 0)
            prefix_sums[s] = prefix_sums.get(s, 0) + 1

        return result


# tests
s = Solution()
assert s.subarraySum([1, 1, 1], 2) == 2
assert s.subarraySum([1, 2, 3], 3) == 2
