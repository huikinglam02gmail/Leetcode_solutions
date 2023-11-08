#
# @lc app=leetcode id=2849 lang=python3
#
# [2849] Determine if a Cell Is Reachable at a Given Time
#

# @lc code=start
class Solution:
    '''
    The minimum time to reach from s to f is max(abs(sx - fx), abs(sy - fy))
    Given extra time, we can hover around the finish point
    The edge case is if sx == fx and sy == fy and t == 1, then we must return false
    '''
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        need = max(abs(sx - fx), abs(sy - fy))
        if need == 0 and t == 1: return False
        return need <= t
# @lc code=end

