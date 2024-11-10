#
# @lc app=leetcode id=3239 lang=python3
#
# [3239] Minimum Number of Flips to Make Binary Grid Palindromic I
#

# @lc code=start
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        result = float("inf")
        current = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            l, r = 0, n - 1
            while l < r:
                if grid[i][l] != grid[i][r]: current += 1
                l += 1
                r -= 1
        result = min(result, current)

        current = 0
        for j in range(n):
            t, b = 0, m - 1
            while t < b:
                if grid[t][j] != grid[b][j]: current += 1
                t += 1
                b -= 1
        result = min(result, current)
        return result
# @lc code=end

