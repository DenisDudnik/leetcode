# https://leetcode.com/problems/zigzag-conversion/

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if numRows == 1:
        #     return s

        # matrix, column_num, idx = [], 0, 0
        # while idx < len(s):
        #     if column_num % (numRows-1) == 0:
        #         sub_str = s[idx:idx + numRows].ljust(numRows)
        #         matrix.append(list(sub_str))
        #     else:
        #         sub_str = s[idx]
        #         matrix.append([" "]*numRows)
        #         matrix[-1][numRows-1-column_num%(numRows-1)] = sub_str[0]
        #     column_num += 1
        #     idx += len(sub_str)
        # transposed_matrix = list(map(list, zip(*matrix)))
        # result = "".join(["".join(x) for x in transposed_matrix]).replace(" ", "")
        # return result
        
        if numRows == 1 or len(s) <= numRows:
            return s
        
        res_list = [""]*numRows
        idx, step = 0, -1
        
        for c in s:
            res_list[idx] += c
            if idx == 0 or idx == numRows-1:
                step *= -1
            idx += step
        return "".join(res_list)
        


if __name__ == "__main__":
    assert Solution().convert(s="PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR"
    assert Solution().convert(s="PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI"
    assert Solution().convert(s="A", numRows=1) == "A"
    assert Solution().convert(s="AB", numRows=1) == "AB"
