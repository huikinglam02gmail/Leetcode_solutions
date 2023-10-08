#
# @lc app=leetcode id=1937 lang=python3
#
# [1937] Maximum Number of Points with Cost
#

# @lc code=start
from typing import List


class Solution:
    '''
    A more advanced version of 1014. Best Sightseeing Pair.
    For row i, if the grid point of the maximum point path is at (i, j), its contribution to the final total is dp[i][j] = points[i][j] + max(dp[i-1][j'] - abs(j - j')). As contribution of each column decrement by one, when we update result in one row, we can scan from right to left and then left to right
    '''
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)
            for j in range(n):
                if j > 0:
                    points[i][j] = max(points[i][j], points[i][j - 1] - 1)
                points[i + 1][j] += points[i][j]
        return max(points[-1])
        
# @lc code=end

