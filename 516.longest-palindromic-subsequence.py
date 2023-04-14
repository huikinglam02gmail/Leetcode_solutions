#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    '''
    dp[i][j] = longest palindromic subsequence within s[i:j+1]
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    if s[i] == s[j]:
                        dp[i][j] = max(dp[i][j], 2 + dp[i+1][j-1])
        return dp[0][len(s)-1]
# @lc code=end

