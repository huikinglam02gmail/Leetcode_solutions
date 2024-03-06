#
# @lc app=leetcode id=3033 lang=python3
#
# [3033] Modify the Matrix
#

# @lc code=start
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            maxEle = -1
            negOnes = []
            for i in range(m):
                maxEle = max(maxEle, matrix[i][j])
                if matrix[i][j] == -1: negOnes.append(i)
            for i in negOnes: matrix[i][j] = maxEle
        return matrix
# @lc code=end

