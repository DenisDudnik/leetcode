# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for idx in range(n):
                nums1[idx] = nums2[idx]
            return
        
        idx = m + n - 1
        while n > 0:
            num2 = nums2[n-1]
            if m == 0 or num2 >= nums1[m-1]:
                nums1[idx] = num2
                n -= 1
            else:
                nums1[idx], nums1[m-1] = nums1[m-1], nums1[idx]
                m -= 1
            idx -= 1



if __name__ == "__main__":
    nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
    id_num = id(nums1)
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]
    assert id_num == id(nums1)

    print("----")
    nums1, m, nums2, n = [1], 1, [], 0
    id_num = id(nums1)
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]
    assert id_num == id(nums1)
    print("----")

    nums1, m, nums2, n = [0], 0, [1], 1
    id_num = id(nums1)
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]
    assert id_num == id(nums1)
    print("----")

    nums1, m, nums2, n = [2,0], 1, [1], 1
    id_num = id(nums1)
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1, 2]
    assert id_num == id(nums1)
