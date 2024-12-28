#
# @lc app=leetcode id=2249 lang=python3
#
# [2249] Count Lattice Points Inside a Circle
#

# @lc code=start
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        searchSpace = [float("inf"), float("inf"), - float("inf"), - float("inf")]
        for x, y, r in circles:
            searchSpace[0] = min(searchSpace[0], x - r)
            searchSpace[1] = min(searchSpace[1], y - r)
            searchSpace[2] = max(searchSpace[2], x + r)
            searchSpace[3] = max(searchSpace[3], y + r)
        
        m, n = searchSpace[2] - searchSpace[0] + 1, searchSpace[3] - searchSpace[1] + 1
        included = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if included[i][j]: continue
                for x, y, r in circles:
                    if (searchSpace[0] + i - x) * (searchSpace[0] + i - x) + (searchSpace[1] + j - y) * (searchSpace[1] + j - y) <= r * r: 
                        included[i][j] = True
                        continue
        
        result = 0
        for i in range(m):
            for j in range(n):
                if included[i][j]: result += 1
        return result
# @lc code=end

