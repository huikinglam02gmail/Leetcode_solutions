#
# @lc app=leetcode id=2139 lang=python3
#
# [2139] Minimum Moves to Reach Target Score
#

# @lc code=start
class Solution:
    '''
    if maxDoubles = 0, give target - 1
    if target % 2 > 0, give 1 + minMoves(target - 1, maxDoubles)
    else give 1 + minMoves(target // 2, maxDoubles - 1)
    '''
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1: return 0
        elif maxDoubles == 0: return target - 1
        elif target % 2 > 0: return 1 + self.minMoves(target - 1, maxDoubles)
        else: return 1 + self.minMoves(target // 2, maxDoubles - 1)
        
# @lc code=end

