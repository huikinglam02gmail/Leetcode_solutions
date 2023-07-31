#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
class Solution:
    '''
    Classic DP string comparison problem
    Build a 2D dp between the strings, with extra position for empty character
    dp[i][j] =  the lowest ASCII sum of deleted characters to make s1[:j] and s2[:i] equal.
    The recursion formula is simple:
    if s1[i] = s2[j]: dp[i][j] = dp[i-1][j-1]
    else: dp[i][j] = min(ord(s2[i]) + dp[i-1][j], ord(s1[j]) + dp[i][j-1])    
    '''

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[float('Inf') for i in range(len(s1)+1)]for j in range(len(s2)+1)]
        dp[0][0] = 0
        for i in range(1,len(s1)+1):
            dp[0][i] = dp[0][i-1] + ord(s1[i-1])
        for i in range(1,len(s2)+1):
            dp[i][0] = dp[i-1][0] + ord(s2[i-1])
        for i in range(1,len(s2)+1):
            for j in range(1, len(s1)+1):
                dp[i][j] = min(dp[i][j], dp[i-1][j] + ord(s2[i-1]), dp[i][j-1] + ord(s1[j-1]))
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        return dp[len(s2)][len(s1)]
# @lc code=end

