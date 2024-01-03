# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        translate = {}
        seen = set()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for c, w in zip(pattern, words):
            t = translate.get(c, None)
            if (t and t != w) or (not t and w in seen):
                return False
            translate[c] = w
            seen.add(w)
        return True


if __name__ == "__main__":
    assert Solution().wordPattern(pattern="abba", s="dog cat cat dog") == True
    assert Solution().wordPattern(pattern="abba", s="dog cat cat fish") == False
    assert Solution().wordPattern(pattern="aaaa", s="dog cat cat dog") == False
    assert Solution().wordPattern(pattern="aaa", s="aa aa aa aa") == False
