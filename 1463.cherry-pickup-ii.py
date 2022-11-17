#
# @lc app=leetcode id=1463 lang=python3
#
# [1463] Cherry Pickup II
#

# @lc code=start
class Solution:
    # DP problem
    # dp(i,j,k) = maximum number of cherries collection using both robots at row i, robot 1 at j and robot 2 at k
    # dp(i, j, k) = grid[i][j] + grid[i][k] + max(dp(i-1, j-1, k), dp(i-1, j, k), dp(i-1, j+1, k), dp(i-1, j-1, k-1), dp(i-1, j, k-1), dp(i-1, j+1, k-1), dp(i-1, j-1, k+1), dp(i-1, j, k+1), dp(i-1, j+1, k+1))
    # if j == k, dp(i,j,k) -= grid[i][j]
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(n)]
        dp[0][n-1] = grid[0][0] + grid[0][n-1]
        result = grid[0][0] + grid[0][n-1]
        for i in range(1, m):
            dpNew = [[-1 for i in range(n)] for j in range(n)]
            for j in range(n):
                for k in range(n):
                    choices = -1
                    if dp[j][k] >= 0:
                        choices = max(choices, dp[j][k])
                    if j > 0 and dp[j-1][k] >= 0:
                        choices = max(choices, dp[j-1][k])
                    if j < n - 1 and dp[j+1][k] >= 0:
                        choices = max(choices, dp[j+1][k])
                    if k > 0 and dp[j][k-1] >= 0:
                        choices = max(choices, dp[j][k-1])
                    if k < n - 1 and dp[j][k+1] >= 0:
                        choices = max(choices, dp[j][k+1])
                    if j > 0 and k > 0 and dp[j-1][k-1] >= 0:
                        choices = max(choices, dp[j-1][k-1])
                    if j < n - 1 and k > 0 and dp[j+1][k-1] >= 0:
                        choices = max(choices, dp[j+1][k-1])
                    if j > 0 and k < n - 1 and dp[j-1][k+1] >= 0:
                        choices = max(choices, dp[j-1][k+1])
                    if j < n - 1 and k < n - 1 and dp[j+1][k+1] >= 0:
                        choices = max(choices, dp[j+1][k+1])
                    if choices >= 0:
                        if j != k:
                            dpNew[j][k] = grid[i][j] + grid[i][k]
                        else:
                            dpNew[j][k] = grid[i][j]
                        dpNew[j][k] += choices
                        result = max(result, dpNew[j][k])
            dp = dpNew
        return result  
# @lc code=end

