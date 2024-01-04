# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        m = n
        while (m != 1) and (m not in cache):
            cache.add(m)
            m = sum((int(x) ** 2 for x in str(m)))

        return m == 1


if __name__ == "__main__":
    assert Solution().isHappy(19) == True
    assert Solution().isHappy(2) == False
    assert Solution().isHappy(7) == True
