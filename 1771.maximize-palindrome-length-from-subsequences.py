#
# @lc app=leetcode id=1771 lang=python3
#
# [1771] Maximize Palindrome Length From Subsequences
#

# @lc code=start
class Solution:
    '''
    First thing we should notice: the longest palindrome possible, must start at word1 and end at word2, and should be the same character.
    Remember the final product is always a subsequence of word1 + word2. We want to find the length of longest palindrome formed from that. We know how to solve Leetcode 516. Longest Palindromic Subsequence. In here, if word1[i] == word2[j], we ask for the longest palindromic subsequence of (word1 + word2)[i + 1: m + j]
    '''
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        m = len(word1)
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        result = 0
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    if s[i] == s[j]:
                        dp[i][j] = max(dp[i][j], 2 + dp[i+1][j-1])
                        if i < m and j >= m:
                            result = max(result, dp[i][j])
        return result
# @lc code=end

