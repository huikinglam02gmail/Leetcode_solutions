#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    Transpose the grid, then compare row by row   
    '''

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transposed.append(row)
        return transposed
    
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed_grid =  self.transpose(grid)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i] == transposed_grid[j]:
                    result += 1
        return result
# @lc code=end

