# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


if __name__ == "__main__":
    assert Solution().twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert Solution().twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
    assert Solution().twoSum(numbers=[-1, 0], target=-1) == [1, 2]
