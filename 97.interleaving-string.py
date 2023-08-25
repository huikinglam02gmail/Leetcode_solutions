#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    '''
    dp[i][j] = s3[:i + j] can be formed by interleaving s1[:i] and s2[:j]
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = s2[j-1] == s3[j-1] and dp[i][j-1]
                elif j == 0:
                    dp[i][j] = s1[i-1] == s3[i-1] and dp[i-1][j]
                else:
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[len(s1)][len(s2)]
# @lc code=end

