# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len, cur_sum, left_idx = len(nums) + 1, 0, 0

        for right_idx, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= target:
                min_len = min(min_len, right_idx - left_idx + 1)
                cur_sum -= nums[left_idx]
                left_idx += 1

        if min_len > len(nums):
            min_len = 0
        print(min_len)
        return min_len


if __name__ == "__main__":
    assert Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert Solution().minSubArrayLen(target=4, nums=[1, 4, 4]) == 1
    assert Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert Solution().minSubArrayLen(target=6, nums=[2, 2, 4, 1]) == 2
