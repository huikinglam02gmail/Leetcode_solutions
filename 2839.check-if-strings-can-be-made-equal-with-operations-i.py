#
# @lc app=leetcode id=2839 lang=python3
#
# [2839] Check if Strings Can be Made Equal With Operations I
#

# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        if s1[2] + s1[1] + s1[0] + s1[3] == s2: return True
        if s1[2] + s1[3] + s1[0] + s1[1] == s2: return True
        if s1[0] + s1[3] + s1[2] + s1[1] == s2: return True
        return False
# @lc code=end

