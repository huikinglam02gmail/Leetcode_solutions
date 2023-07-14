#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#

# @lc code=start
class Solution:
    '''
    simple DP question
    dp[i] = a hash table of length of LAS for arr[:i+1], ending with different numbers
    a new number can only contribute to 1 of thems    
    '''

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        maxSeen = 0
        for num in arr:
            dp[num] = max(dp.get(num,0), 1 + dp.get(num - difference, 0))
            maxSeen = max(maxSeen, dp[num])
        return maxSeen
# @lc code=end

