#
# @lc app=leetcode id=1895 lang=python3
#
# [1895] Largest Magic Square
#

# @lc code=start
from typing import List


class Solution:
    '''
    we need to keep calculating row, column and diagonal sum, so prepare them.
    To be a magic square of size k with bottom right point (i, j), these are the conditions, for a number S:
    1. rowSum(i1, j) - rowSum(i1, j - k) = S for i1 = i - k - 1,... , i
    2. colSum(i, j1) - colSum(i - k, j1) = S for j1 = j - k - 1,... , j
    3. leftDiagonalSum(i, j - 1 - k) - leftDiagonalSum(i - k, j + 1) = S
    4. rightDiagonalSum(i, j) - rightDiagonalSum(i - k, j - k) = S
    '''
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rowSum = [[0 for j in range(n + 1)] for i in range(m)]
        colSum = [[0 for j in range(n)] for i in range(m + 1)]
        leftDiagonalSum =  [[0 for j in range(n + 1)] for i in range(m + 1)]
        rightDiagonalSum =  [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m):
            for j in range(n):
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j]
                colSum[i + 1][j] = colSum[i][j] + grid[i][j]
                leftDiagonalSum[i + 1][j] = leftDiagonalSum[i][j + 1] + grid[i][j]
                rightDiagonalSum[i + 1][j + 1] = rightDiagonalSum[i][j] + grid[i][j]
        
        for k in range(min(m, n), 0, -1):
            for i in range(m - 1, k - 2 , -1):
                for j in range(n - 1, k - 2, -1):
                    S = rightDiagonalSum[i + 1][j + 1] - rightDiagonalSum[i + 1 - k][j + 1 - k]
                    allS = True
                    allS = (allS and (leftDiagonalSum[i + 1][j + 1 - k] - leftDiagonalSum[i + 1 - k][j + 1] == S))
                    for l in range(i - k + 1, i + 1, 1):
                        allS = (allS and (rowSum[l][j + 1] - rowSum[l][j + 1 - k] == S))
                    for l in range(j - k + 1, j + 1, 1):
                        allS = (allS and (colSum[i + 1][l] - colSum[i + 1 - k][l] == S))
                    if allS:
                        return k
        return -1
# @lc code=end

