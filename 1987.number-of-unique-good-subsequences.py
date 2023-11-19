#
# @lc app=leetcode id=1987 lang=python3
#
# [1987] Number of Unique Good Subsequences
#

# @lc code=start
class Solution:
    '''
    This is very similar to Leetcode 940. In this case a-z becomes 0 or 1.
    Let's recap the key idea in 940:
    Given each new character c, we can form distinct subsequence by itself or previous subsequence + c
    In here the 1 + condition only applies with c == "1"
    At the end, remember to check if "0" is in binary
    '''
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp, current, MOD, add1 = [0]*2, 0, pow(10, 9) + 7, 0
        for c in binary:
            dp[int(c)] = (int(c) + current) % MOD
            current = sum(dp) % MOD
            if int(c) == 0: add1 = 1
        return current + add1
# @lc code=end

