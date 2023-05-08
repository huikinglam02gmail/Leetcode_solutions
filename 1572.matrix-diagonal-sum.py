#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            result += mat[i][i]
            result += mat[i][len(mat)-1-i]
        if len(mat) % 2 == 1:
            result -= mat[len(mat)//2][len(mat)//2]
        return result
# @lc code=end

