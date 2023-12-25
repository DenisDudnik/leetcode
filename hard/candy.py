# https://leetcode.com/problems/candy/

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        candies[0] = 1
        for idx in range(1, len(ratings)):
            if ratings[idx] > ratings[idx-1]:
                candies[idx] = candies[idx-1] + 1
            else:
                candies[idx] = 1
        
        for idx in range(2, len(ratings)+1):
            if ratings[-idx] > ratings[-(idx-1)]:
                if candies[-idx] <= candies[-(idx-1)]:
                    candies[-idx] = candies[-(idx-1)] + 1
        print(f"{ratings=} {candies=} {sum(candies)=}")

        return sum(candies)


if __name__ == "__main__":
    assert Solution().candy([1,3,4,5,2]) == 11
    assert Solution().candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]) == 42
    assert Solution().candy([1,0,2]) == 5
    assert Solution().candy([1,2,2]) == 4