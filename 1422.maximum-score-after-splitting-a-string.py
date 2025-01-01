#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        totalZeros = s.count('0')
        totalOnes = n - totalZeros
        score, zeros = 0, 0
        for i in range(n-1):
            if s[i] == '0': zeros += 1
            score = max(score, zeros + totalOnes - (i + 1 - zeros))
        return score
        
# @lc code=end

