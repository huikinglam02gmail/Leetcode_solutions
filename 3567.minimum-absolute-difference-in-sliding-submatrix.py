#
# @lc app=leetcode id=3567 lang=python3
#
# [3567] Minimum Absolute Difference in Sliding Submatrix
#

# @lc code=start
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        result = [[0 for _ in range(len(grid[0]) - k + 1)] for _ in range(len(grid) - k + 1)]
        for i in range(len(grid) - k + 1):
            for j in range(len(grid[0]) - k + 1):
                current = set()
                for i1 in range(i, i + k):
                    for j1 in range(j, j + k):
                        current.add(grid[i1][j1])
                currentList = sorted(current)
                if len(current) > 1: result[i][j] = min([currentList[k + 1] - currentList[k] for k in range(len(current) - 1)])
        return result

# @lc code=end
