# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split('/')
        res = []
        for folder in folders:
            if folder == ".." and res:
                res.pop()
            if folder and folder not in (".", ".."):
                res.append(folder)
        return "/" + "/".join(res)


if __name__ == "__main__":
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/../") == "/"
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"
