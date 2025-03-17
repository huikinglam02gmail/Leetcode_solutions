#
# @lc app=leetcode id=2746 lang=python3
#
# [2746] Decremental String Concatenation
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i][start][end] = possible concatenated string starting with start and ending with end
    '''
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        dp = [[float("inf") for j in range(26)] for i in range(26)]
        dp[ord(words[0][0]) - ord('a')][ord(words[0][-1]) - ord('a')] = len(words[0])
        for i in range(1, len(words)):
            dpNew = [[float("inf") for k in range(26)] for j in range(26)]
            start = ord(words[i][0]) - ord('a')
            end = ord(words[i][-1]) - ord('a')
            for j in range(26):
                for k in range(26):
                    if end == k: dpNew[start][j] = min(dpNew[start][j], len(words[i]) + dp[k][j] - 1)
                    else: dpNew[start][j] = min(dpNew[start][j], len(words[i]) + dp[k][j])
                    if start == j: dpNew[k][end] = min(dpNew[k][end], len(words[i]) + dp[k][j] - 1)
                    else: dpNew[k][end] = min(dpNew[k][end], len(words[i]) + dp[k][j])
            dp = dpNew.copy()
        result = float("inf")
        for j in range(26):
            for k in range(26):
                result = min(result, dp[j][k])
        return result


            
        
# @lc code=end

