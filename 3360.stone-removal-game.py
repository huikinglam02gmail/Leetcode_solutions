#
# @lc app=leetcode id=3360 lang=python3
#
# [3360] Stone Removal Game
#

# @lc code=start
class Solution:
    def canWin(self, remain, target, whoseTurn):
        if target > remain: return whoseTurn == 1
        return self.canWin(remain - target, target - 1, 1 - whoseTurn)
    
    def canAliceWin(self, n: int) -> bool:
        return self.canWin(n, 10, 0)
        
# @lc code=end

