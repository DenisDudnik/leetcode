# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for idx in range(len(prices)-1):
            day_profit = 0 if prices[idx+1] <= prices[idx] else prices[idx+1] - prices[idx]
            total_profit += day_profit

        return total_profit


if __name__ == "__main__":
    assert Solution().maxProfit([7,1,5,3,6,4]) == 7
    assert Solution().maxProfit([1,2,3,4,5]) == 4
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    assert Solution().maxProfit([7]) == 0
