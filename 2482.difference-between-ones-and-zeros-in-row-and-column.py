#
# @lc app=leetcode id=2482 lang=python3
#
# [2482] Difference Between Ones and Zeros in Row and Column
#

# @lc code=start
from typing import List


class Solution:
    '''
    onesRow[i] = n - zerosRow[i]
    onesCol[j] = m - zerosCol[j]
    diff[i][j] = n - 2 * zerosRow[i] + m - 2 * zerosCol[j]
    '''
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        zerosRow, zerosCol = [0] * m, [0] * n
        diff = [[m + n for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: 
                    zerosRow[i] += 1
                    zerosCol[j] += 1
        for i in range(m):
            for j in range(n):
                diff[i][j] -= 2 * (zerosRow[i] + zerosCol[j])
        return diff
# @lc code=end

