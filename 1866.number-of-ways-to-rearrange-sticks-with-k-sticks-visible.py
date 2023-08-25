#
# @lc app=leetcode id=1866 lang=python3
#
# [1866] Number of Ways to Rearrange Sticks With K Sticks Visible
#

# @lc code=start
class Solution:
    '''
    Consider if we have set up n - 1 sticks, we are given n.
    Then If we put stick n at the last of previous possible sticks, we will get 1 more stick visble from left.
    ans[n][k] += ans[n - 1][k - 1]
    Now suppose we put in the longest stick in front. Then the last stick could be out of n - 1 choices. The remaining sticks is the same question as having n - 1 sticks and need k visible, as we know the stick n is in front of it. ans[n][k] += (n - 1) * ans[n - 1][k]
    Base Case: k <= n, dp[k][k] = 1 and dp[i][1] = 1
    '''
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        MOD = pow(10, 9) + 7
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] += dp[i - 1][j - 1]
                    dp[i][j] %= MOD
                    dp[i][j] += (i - 1) * dp[i - 1][j]
                    dp[i][j] %= MOD
        return dp[n][k]
# @lc code=end

