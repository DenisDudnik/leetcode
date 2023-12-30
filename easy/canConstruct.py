# https://leetcode.com/problems/ransom-note/


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazine_counter = Counter(magazine)
        ransomNote_counter = Counter(ransomNote)
        for key in ransomNote_counter:
            if (
                key not in magazine_counter
                or magazine_counter[key] < ransomNote_counter[key]
            ):
                return False
        return True


if __name__ == "__main__":
    assert Solution().canConstruct(ransomNote="a", magazine="b") == False
    assert Solution().canConstruct(ransomNote="aa", magazine="ab") == False
    assert Solution().canConstruct(ransomNote="aa", magazine="aab") == True
