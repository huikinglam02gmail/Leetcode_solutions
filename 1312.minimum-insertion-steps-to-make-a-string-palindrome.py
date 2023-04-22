#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
class Solution:
    '''
    1 <= s.length <= 500
    O(N^2) algorithm should be acceptable
    In order to insert characters and to make a string become a palindrome, the minimum insertion steps should be to those characters outside the maximum palindromic subsequence in s
    So, refer to 516. Longest Palindromic Subsequence and return len(s) - len(LPS)    
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
    
    
    def minInsertions(self, s: str) -> int:
        return len(s) - self.longestPalindromeSubseq(s)
          
# @lc code=end

