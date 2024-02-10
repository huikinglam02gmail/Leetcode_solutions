#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    '''
    To count, we count number of Trues in dp:
    dp[i][j] = is s[i:j + 1] a palindrome?
    dp[i][j] if s[j] == s[i] and dp[i + 1][j - 1]
    '''
    def countSubstrings(self, s: str) -> int:
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        count = 0
        n = len(s)
        for j in range(len(s)):
            for i in range(j,-1,-1):
                dp[i][j] = (s[i] == s[j])
                if 0 <= i + 1 <= j - 1 < n: dp[i][j] &= dp[i + 1][j - 1]
                if dp[i][j]: count += 1
        return count
# @lc code=end

