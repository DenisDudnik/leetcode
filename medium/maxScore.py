# https://leetcode.com/problems/maximum-subsequence-score/
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_score, nums1_sum = 0, 0
        heap = []
        nums = list(zip(nums1, nums2))
        nums.sort(key=lambda x: x[1], reverse=True)

        for num in nums:
            heappush(heap, num[0])
            nums1_sum += num[0]
            if len(heap) > k:
                nums1_sum -= heappop(heap)
            if len(heap) == k:
                max_score = max(max_score, nums1_sum * num[1])
        print(max_score)
        return max_score


if __name__ == "__main__":
    assert Solution().maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3) == 12
    assert Solution().maxScore(nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1) == 30
    assert (
        Solution().maxScore(
            nums1=[
                93,
                463,
                179,
                2488,
                619,
                2006,
                1561,
                137,
                53,
                1765,
                2304,
                1459,
                1768,
                450,
                1938,
                2054,
                466,
                331,
                670,
                1830,
                1550,
                1534,
                2164,
                1280,
                2277,
                2312,
                1509,
                867,
                2223,
                1482,
                2379,
                1032,
                359,
                1746,
                966,
                232,
                67,
                1203,
                2474,
                944,
                1740,
                1775,
                1799,
                1156,
                1982,
                1416,
                511,
                1167,
                1334,
                2344,
            ],
            nums2=[
                345,
                229,
                976,
                2086,
                567,
                726,
                1640,
                2451,
                1829,
                77,
                1631,
                306,
                2032,
                2497,
                551,
                2005,
                2009,
                1855,
                1685,
                729,
                2498,
                2204,
                588,
                474,
                693,
                30,
                2051,
                1126,
                1293,
                1378,
                1693,
                1995,
                2188,
                1284,
                1414,
                1618,
                2005,
                1005,
                1890,
                30,
                895,
                155,
                526,
                682,
                2454,
                278,
                999,
                1417,
                1682,
                995,
            ],
            k=42,
        )
        == 26653494
    )
