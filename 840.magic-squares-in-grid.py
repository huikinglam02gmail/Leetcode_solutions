#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
from typing import List


class Solution:
    '''
    Elements in magic square must include 1 to 9
    The center of a magic square must be 5
    So, search for 5
    Check its 8 neighbourhood    
    '''
    def ismagic(self, matrix):
        flattened = []
        for row in matrix:
            for i in row:
                flattened.append(i)
        flattened_string = "".join([str(x) for x in sorted(flattened)])
        if flattened_string != "123456789": return False

        for i in range(3):
            j_sum = 0
            for j in range(3):
                j_sum += matrix[i][j]
            if j_sum != 15: return False
        for j in range(3):
            i_sum = 0
            for i in range(3): i_sum += matrix[i][j]
            if i_sum != 15: return False
        if matrix[0][0] + matrix[1][1] + matrix[2][2] != 15: return False
        if matrix[0][2] + matrix[1][1] + matrix[2][0] != 15: return False
        return True
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                matrix = []
                for k in range(-1, 2): matrix.append(grid[i + k][j - 1:j + 2])
                if self.ismagic(matrix): count += 1
        return count
# @lc code=end

