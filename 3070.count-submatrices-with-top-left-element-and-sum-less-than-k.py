#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        current = [0] * (n + 1)
        for i in range(m):
            prefix = 0
            for j in range(n):
                prefix += grid[i][j]
                current[j + 1] += prefix
            count += bisect.bisect_right(current, k) - 1
        return count


# @lc code=end

