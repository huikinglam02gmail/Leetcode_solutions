#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        seen.add((0,0))
        x, y = 0, 0
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'E':
                x += 1
            elif c == 'S':
                y -= 1
            else:
                x -= 1
            if (x, y) in seen:
                return True
            else:
                seen.add((x,y))
        return False
# @lc code=end

