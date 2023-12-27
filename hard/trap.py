# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        v, left_idx, right_idx, left, right = 0, 1, len(height) - 2, 0, len(height) - 1

        while left_idx <= right_idx:
            if height[left] <= height[right]:
                if height[left_idx] >= height[left]:
                    left = left_idx
                v += height[left] - height[left_idx]
                left_idx += 1
            else:
                if height[right_idx] >= height[right]:
                    right = right_idx
                v += height[right] - height[right_idx]
                right_idx -= 1

        print(v)
        return v


if __name__ == "__main__":
    assert Solution().trap([1]) == 0
    assert Solution().trap([1, 9]) == 0
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
