#
# @lc app=leetcode id=2938 lang=python3
#
# [2938] Separate Black and White Balls
#

# @lc code=start
class Solution:
    '''
    Final state is known. Just add indices of 0s in the final state - indices of 0 in the current state
    '''
    def minimumSteps(self, s: str) -> int:
        result = 0
        countZero = 0
        for i, c in enumerate(s):
            if c == "0":
                result += i - countZero
                countZero += 1
        return result
        
# @lc code=end

