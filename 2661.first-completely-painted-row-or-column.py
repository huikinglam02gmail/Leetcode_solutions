#
# @lc app=leetcode id=2661 lang=python3
#
# [2661] First Completely Painted Row or Column
#

# @lc code=start
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0 for i in range(m)]
        cols = [0 for j in range(n)]
        coord = {}
        for i in range(m):
            for j in range(n):
                coord[mat[i][j]] = [i, j]
        for i, num in enumerate(arr):
            rows[coord[num][0]] += 1
            cols[coord[num][1]] += 1
            if rows[coord[num][0]] == n:
                return i
            elif cols[coord[num][1]] == m:
                return i
        return -1
        # @lc code=end

