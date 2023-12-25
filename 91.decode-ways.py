#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    '''
    A DP question, as it can be broken in subproblems
    Use a 2D dp with 2 rows and len(s) columns to represent the number of decoding ways up to index i. The 0th row represent the decoding ways when considering the current s as a single digit whereas 1st row represent the decoding ways when considering the current s as last of two digits
    In this problem, "0" is a special case: it can only be in "10" and "20"    
    '''
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0": return 0
        dp = [[0 for j in range(len(s))] for i in range(2)]
        dp[0][0] = 1
        for i in range(1, n):
            if s[i] == "0":
                if s[i - 1] in ["1", "2"]:
                    dp[1][i] += dp[0][i - 1]
            else:
                '''
                Can use both single and double characters before
                e.g. "127" could be "1"+"2"+"7" and "12"+"7"                
                '''
                dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
                if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] in ["1","2","3","4","5","6"]):
                    '''
                    Can use both single and double characters before
                    e.g. "1126" could be "11"+"26" and "1"+"1"+"26"                       
                    '''                    
                    if i == 1:
                        dp[1][i] = 1
                    else:
                        dp[1][i] = dp[1][i - 2] + dp[0][i - 2]
        return dp[0][n - 1] + dp[1][n - 1]
# @lc code=end

