#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from typing import List


class Solution:        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        dfs algorithm to traverse the dp array        
        '''
        def dfs(col, string):
            if col == len(s):
                result.append(string[:-1])
                return
            else:
                for i in range(col, len(s), 1):
                    if dp[col][i] and s[col:i+1] in hash_set: dfs(i+1, string + s[col:i+1] + " ")
                
        hash_set = set()
        for c in wordDict: hash_set.add(c)
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j,-1,-1):
                if i == j: dp[i][j] = s[i] in hash_set
                else:
                    for k in range(j): dp[i][j] = dp[i][j] or (dp[i][k] and dp[k+1][j])
                    if not dp[i][j]: dp[i][j] = s[i:j+1] in hash_set
        
        if not dp[0][len(s)-1]:
            return []
        else:
            result = []            
            dfs(0,"")
            return result
# @lc code=end

