# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        subset_sum = sum(nums) // k
        if nums[0] > subset_sum or sum(nums) % k:
            return False
        print(f"{subset_sum}")

        subsets_sums = [subset_sum for _ in range(k)]

        def backtrack(index: int) -> bool:
            if index == len(nums):
                return sum(subsets_sums) == 0
            print(f"{index=} {subsets_sums=} {nums[index]=}")
            for i in range(k):
                if i > 0 and subsets_sums[i - 1] == subsets_sums[i]:
                    continue
                if subsets_sums[i] - nums[index] >= 0:
                    subsets_sums[i] -= nums[index]
                    if backtrack(index + 1):
                        return True
                    subsets_sums[i] += nums[index]
            return False

        return backtrack(0)


if __name__ == "__main__":
    solution = Solution()

    def check_case(nums: List[int], k: int, expected: bool):
        result = solution.canPartitionKSubsets(nums, k)
        assert result == expected, f"Failed for nums={nums}, k={k}\nExpected: {expected}, Got: {result}"

    # Пример 1
    check_case([4, 3, 2, 3, 5, 2, 1], 4, True)

    # Пример 2
    check_case([1, 2, 3, 4], 3, False)

    print("All test cases passed.")
