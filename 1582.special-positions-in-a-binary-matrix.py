#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        row_sum = [0]*len(mat)
        column_sum = [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row_sum[i] += mat[i][j]
                column_sum[j] += mat[i][j]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_sum[i] == 1 and column_sum[j] == 1:
                    result += 1
        return result
# @lc code=end

