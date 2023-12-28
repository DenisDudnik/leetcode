# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_substr = len(words)*len(words[0])
        len_word = len(words[0])
        counter_words = Counter(words)
        idx = 0
        res = []
        while idx <= len(s) - len_substr:
            substr = s[idx:idx+len_substr]
            counter_substr = Counter([substr[x:x+len_word] for x in range (0, len_substr, len_word)])
            if counter_words == counter_substr:
                res.append(idx)
            idx += 1
        return res


if __name__ == "__main__":
    assert Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]) == [0,9]
    assert Solution().findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]) == []
    assert Solution().findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]) == [6,9,12]
    assert Solution().findSubstring(s = "lingmindraboofooowingdingbarrwingmonkeypoundcake", words = ["fooo","barr","wing","ding","wing"]) == [13]
