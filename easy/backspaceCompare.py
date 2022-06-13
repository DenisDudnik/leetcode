from itertools import zip_longest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_lst, t_lst = [], []
        for el in zip_longest(s, t):
            if el[0] == "#":
                try:
                    s_lst.pop()
                except:
                    pass
            else:
                if el[0] != None:
                    s_lst.append(el[0])

            if el[1] == "#":
                try:
                    t_lst.pop()
                except:
                    pass
            else:
                if el[1] != None:
                    t_lst.append(el[1])
        return s_lst == t_lst


if __name__ == "__main__":
    assert Solution().backspaceCompare(s="ab#c", t="ad#c") == True
    assert Solution().backspaceCompare(s="ab##", t="c#d#") == True
    assert Solution().backspaceCompare(s="a#c", t="b") == False
    assert Solution().backspaceCompare(s="a##c", t="b##c#c") == True
