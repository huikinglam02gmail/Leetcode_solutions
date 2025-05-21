#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = False
        column = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0: column = True
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0: row = True        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        if row:
            for j in range(len(matrix[0])): matrix[0][j] = 0
        if column:
            for j in range(len(matrix)): matrix[j][0] = 0       
# @lc code=end

