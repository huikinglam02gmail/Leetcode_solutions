#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
class Solution:
    '''
    Shortest Common Supersequence
    = extra bit + parts containing longest common subsequence + extra bit
    So, first copy the code from Leetcode 1143. Longest Common Subsequence
    Then we can modify the code to store the LCS in the DP matrix    
    '''
 
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [["" for i in range(len(str1)+1)] for j in range(len(str2)+1)]
        for i in range(1, len(str2)+1):
            for j in range(1, len(str1)+1):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], key = len)
                if str1[j-1] == str2[i-1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1] + str1[j-1], key = len)
       
        lcs, i, j = dp[-1][-1], 0, 0
        result = ""
        for c in lcs:
            while c != str1[i]:
                result += str1[i]
                i += 1
            while c != str2[j]:
                result += str2[j]
                j += 1
            result += c
            i += 1
            j += 1
        return result + str1[i:] + str2[j:]
# @lc code=end

