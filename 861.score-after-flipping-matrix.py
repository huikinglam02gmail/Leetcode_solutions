#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
from typing import List


class Solution:
    '''
    Greedy approach
    First column is larger than sum of all on the right
    1000 = 8 > 0111 = 7
    Therefore, one must flip all rows with first column 0s to 1s
    Then for each column, count max(# 1s, # 0s)    
    '''
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        score = 0
        for j in range(n):
            col = [grid[i][j] for i in range(m)]
            score += (1 << (n-1-j))* max(col.count(1), col.count(0))
        return score
# @lc code=end

