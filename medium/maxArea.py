# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx, right_idx, vmax = 0, len(height) - 1, 0
        while left_idx < right_idx:
            v = min(height[left_idx], height[right_idx]) * (right_idx - left_idx)
            vmax = max(v, vmax)
            if height[left_idx] <= height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        return vmax


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
