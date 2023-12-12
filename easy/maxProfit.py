# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price, delta = prices[0], 0, 0
        for price in prices:
            if price < min_price:
                delta = max(delta, max_price - min_price)
                min_price = price
                max_price = price
            elif price > max_price:
                max_price = price
                delta = max(delta, max_price - min_price)
        print(delta)
        return delta


if __name__ == "__main__":
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    assert Solution().maxProfit([7,2,5,3,6,4,1]) == 4
    assert Solution().maxProfit([7,2,6,1,4,4,1]) == 4
