#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#

# @lc code=start
class Solution:
    '''
    Given each new character c, we can form distinct subsequence by itself or previous subsequence + c
    '''
    def distinctSubseqII(self, s: str) -> int:
        dp, current, MOD = [0]*26, 0, pow(10, 9) + 7
        for c in s:
            dp[ord(c) - ord('a')] = (1 + current) % MOD
            current = sum(dp) % MOD
        return current
        
# @lc code=end

