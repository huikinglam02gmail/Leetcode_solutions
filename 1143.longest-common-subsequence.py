#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    '''
    Classic DP problem
    dp[i][j] = LCS length between text1[:i] and text2[:j]     
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2)+ 1)]
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = max(dp[i][j],dp[i - 1][j - 1] + 1)
        return dp[len(text2)][len(text1)]
# @lc code=end

