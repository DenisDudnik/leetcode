# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])

        s = s.strip()
        pos = s.rfind(" ")
        return len(s) - pos - 1 if pos > -1 else len(s)

        # length = 0
        # for symbol in s[::-1]:
        #     if not length and symbol == " ":
        #         continue
        #     elif symbol != " ":
        #         length += 1
        #     else:
        #         return length
        # return length


if __name__ == "__main__":
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
