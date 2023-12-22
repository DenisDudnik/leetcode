# https://leetcode.com/problems/text-justification/

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines, line_num = [(0, 0)], 0   #   [(first word in line index, letters count in line w/o spaces)]
        
        for idx in range(len(words)):
            if lines[line_num][1] + len(words[idx]) + (idx-lines[line_num][0]) <= maxWidth:
                lines[line_num] = (lines[line_num][0], lines[line_num][1]+len(words[idx]))
            else:
                line_num += 1
                lines.append((idx, len(words[idx])))

        result = []
        for line_num in range(len(lines)-1):
            words_in_line = lines[line_num+1][0] - lines[line_num][0]
            
            if words_in_line < 2:
                result.append(words[lines[line_num][0]] + ' '*(maxWidth-len(words[lines[line_num][0]])))
            else:
                spaces = [' '*((maxWidth-lines[line_num][1])//(words_in_line-1))] * (words_in_line-1)
                for i in range((maxWidth-lines[line_num][1])%(words_in_line-1)):
                    spaces[i] += " "
                res_line = words[lines[line_num][0]]
                for i, space in enumerate(spaces):
                    res_line += space + words[lines[line_num][0]+i+1]
                result.append(res_line)
        
        res_line = " ".join(words[lines[-1][0]:])
        res_line = res_line + ' '*(maxWidth-len(res_line))
        result.append(res_line)

        return result
                
                


if __name__ == "__main__":
    assert Solution().fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    ) == ["This    is    an", "example  of text", "justification.  "]
    assert Solution().fullJustify(
        words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16
    ) == ["What   must   be", "acknowledgment  ", "shall be        "]
    assert Solution().fullJustify(
        words=[
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        maxWidth=20,
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
