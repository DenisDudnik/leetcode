# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1:
            return True

        replace = {}

        for c_s, c_t in zip(s, t):
            c = replace.get(c_s, None)
            if (c and c != c_t) or (not c and c_t in replace.values()):
                return False
            replace[c_s] = c_t
        return True


if __name__ == "__main__":
    assert Solution().isIsomorphic(s="egg", t="add") == True
    assert Solution().isIsomorphic(s="foo", t="bar") == False
    assert Solution().isIsomorphic(s="paper", t="title") == True
    assert Solution().isIsomorphic(s="badc", t="baba") == False
