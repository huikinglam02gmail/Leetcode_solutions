#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

# @lc code=start
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        appear = set([i for i in range(1, n * n + 1)])
        result = [-1, -1]
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in appear:  result[0] = grid[i][j]
                else: appear.remove(grid[i][j])
        result[1] = list(appear)[0]
        return result
# @lc code=end

