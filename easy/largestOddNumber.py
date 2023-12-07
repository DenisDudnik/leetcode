# https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        ODD_NUMS = ('1', '3', '5', '7', '9')
        right_index = -1
        for odd_num in ODD_NUMS:
            max_index = num.rfind(odd_num)
            if max_index > right_index:
                right_index = max_index
        return num[:right_index+1]


if __name__ == "__main__":
    assert Solution().largestOddNumber(num = "52") == "5"
    assert Solution().largestOddNumber(num = "4206") == ""
    assert Solution().largestOddNumber(num = "35427") == "35427"
    assert Solution().largestOddNumber(num = "354272") == "35427"