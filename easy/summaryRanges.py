# https://leetcode.com/problems/summary-ranges/

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        res = [str(nums[0])]
        start_idx = 0
        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx - 1] > 1:
                if idx - 1 > start_idx:
                    res[-1] += f"->{nums[idx-1]}"
                res.append(str(nums[idx]))
                start_idx = idx
        if len(nums) - 1 > start_idx:
            res[-1] += f"->{nums[-1]}"
        print(res)
        return res


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0]) == ["0"]
