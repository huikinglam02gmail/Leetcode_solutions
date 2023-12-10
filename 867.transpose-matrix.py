#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transposed.append(row)
        return transposed
# @lc code=end

