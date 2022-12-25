#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    # A DP problem which requires drawing out the diagrams for good understanding!
    # The key is to set up a good definition of the dp array
    # I chose the following:
    # dp[k][j] = number of unique configuration with the element at the last column j
    # k = 0:
    # X
    # X
    # k = 1:
    # XX
    # k = 2:
    # Left is XX Right is X
    #         X ,        XX
    # k = 3:
    # Left is X  Right is XX
    #         XX,          X
    # k = 4:
    # Left is X  Right is X
    #         XX,        XX
    # k = 5:
    # Left is XX  Right is XX
    #         X,            X
    # If you tabulate it on a spreadsheet (you should!), one would find that k = 3 is the practically same as k = 2, and k = 5 is the same as k = 4
    # Therefore I reduced the DP to be more concise, with case 0, 1, 2, 3
    # DP relation:
    # dp[0][0] = 1, and dp[0][j] = sum(dp[:][j-1])
    # dp[1][1] = 1, and dp[1][j] = sum(dp[:][j-2])
    # dp[2][2] = 1, and dp[2][j] = dp[2][j-2] + sum(dp[:][j-3])
    # dp[3][3] = 1, and dp[3][j] = dp[3][j-2] + sum(dp[:][j-4])
    # Now we see dp[1][j] == dp[0][j-1]
    #            dp[3][j] == dp[2][j-1]
    # Furthermore, from tabulation, we see something even more interesting:
    # dp[0][j] = dp[2][j+2] - dp[2][j]
    # dp[1][j] = dp[0][j-1] = dp[2][j+1] - dp[2][j-1]
    # dp[3][j] = dp[2][j-1]
    # Sum them up, the ans we want is dp[0][j] + dp[1][j] + 2*dp[2][j] + 2*dp[3][j]
    # dp[2][j+2] + dp[2][j+1] + dp[2][j] + dp[2][j-1]
    # So the final result is somewhat like a rolling hash sum with window size of 4
    
    def numTilings(self, n: int) -> int:
        MOD = pow(10,9) + 7
        dp = [0 for i in range(max(4,n+3))]
        for i in range(4):
            if i > 1:
                dp[i] = 1
        result = 1
        for i in range(4, n+3):
            if i > 4:
                result -= dp[i-5]
            result += dp[i-1]
            dp[i] = dp[i-2] + result
            result %= MOD
            dp[i] %= MOD
        return result
# @lc code=end

