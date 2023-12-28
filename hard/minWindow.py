# https://leetcode.com/problems/minimum-window-substring/


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict, win_dict, left, right, best, sub, found = {}, {}, 0, 0, None, "", 0
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        for idx, c in enumerate(s):
            right = idx
            if c in t_dict:
                win_dict[c] = win_dict.get(c, 0) + 1
                if t_dict[c] >= win_dict[c]:
                    found += 1
            if found == len(t):
                sub = s[left : right + 1]
                for sub_c in sub:
                    if sub_c not in win_dict:
                        left += 1
                    elif t_dict[sub_c] < win_dict[sub_c]:
                        left += 1
                        win_dict[sub_c] -= 1
                    else:
                        break
                if not best:
                    best = s[left : right + 1]
                elif len(best) > right - left + 1:
                    best = s[left : right + 1]
                if s[left] in win_dict:
                    win_dict[s[left]] -= 1
                    found -= 1
                left += 1
        return best or ""


if __name__ == "__main__":
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="a", t="a") == "a"
    assert Solution().minWindow(s="a", t="aa") == ""
