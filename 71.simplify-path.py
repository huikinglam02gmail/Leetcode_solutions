#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    '''
    Split path by /. Different cases: 
    1. "." and "//", "///" etc.means nothing. 
    3. "..": pop existing entry
    '''
    def simplifyPath(self, path: str) -> str:
        pathSplit = path.split('/')
        result = []
        for c in pathSplit:
            if c == "..":
                if result:
                    result.pop()
            elif c != "" and c != ".":
                result.append(c)
        return "/" + "/".join(result)
# @lc code=end

