#
# @lc app=leetcode id=3407 lang=python3
#
# [3407] Substring Matching Pattern
#

# @lc code=start
class Solution:    
    def hasMatch(self, s: str, p: str) -> bool:
        pSplit = p.split("*")
        for i in range(len(s) + 1):
            left = len(pSplit[0]) == 0
            right = len(pSplit[1]) == 0
            left |= pSplit[0] in s[:i]
            right |=  pSplit[1] in s[i:]
            if left and right: return True
        return False

# @lc code=end
