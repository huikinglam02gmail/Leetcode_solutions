#
# @lc app=leetcode id=1878 lang=python3
#
# [1878] Get Biggest Three Rhombus Sums in a Grid
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= m, n <= 50
    can do brute force with each point as the top point
    '''
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = set()
        for i in range(m):
            for j in range(n):
                maxSize = (m - 1 - i) // 2
                trueMaxSize = 0
                j1, j2 = j, j
                while trueMaxSize <= maxSize and j1 < n and j2 >= 0:
                    trueMaxSize += 1
                    j1 += 1
                    j2 -= 1
                for k in range(trueMaxSize):
                    x, y = i, j
                    current = 0
                    for l in range(k):
                        x += 1
                        y += 1
                        current += grid[x][y]
                    for l in range(k):
                        x += 1
                        y -= 1
                        current += grid[x][y]
                    for l in range(k):
                        x -= 1
                        y -= 1
                        current += grid[x][y]
                    for l in range(k):
                        x -= 1
                        y += 1
                        current += grid[x][y]
                    if k > 0:
                        result.add(current)
                    else:
                        result.add(grid[x][y])
        result = sorted(result, key = lambda x: -x)
        return result[:3]
        
# @lc code=end

