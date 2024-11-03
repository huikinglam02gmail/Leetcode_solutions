#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    '''
    This question is asking whether goal is made up of substring of s reorganized
    since string length is short, just use Python string comparison
    '''
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        return goal in s + s
        
        
# @lc code=end

