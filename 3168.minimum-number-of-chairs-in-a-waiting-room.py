#
# @lc app=leetcode id=3168 lang=python3
#
# [3168] Minimum Number of Chairs in a Waiting Room
#

# @lc code=start
class Solution:
    '''
    max pos balance seen so far
    '''
    def minimumChairs(self, s: str) -> int:
        result = 0
        current = 0
        for c in s:
            if c == "E": current += 1
            else: current -= 1
            result = max(result, current)
        return result
        
# @lc code=end

