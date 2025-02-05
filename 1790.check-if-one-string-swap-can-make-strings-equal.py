#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatch = []
        for i in range(len(s1)):
            if s1[i] != s2[i]: mismatch.append(i)
            if len(mismatch) > 2: return False
        if len(mismatch) == 0: return True
        elif len(mismatch) == 2: return s1[mismatch[0]] == s2[mismatch[1]] and s1[mismatch[1]] == s2[mismatch[0]]
        else: return False
            
# @lc code=end

