#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#

# @lc code=start
from typing import List


class Solution:
    '''
    We surely won't cook dishes with very low satisfaction. When to stop?
    # First sort satisfaction, then cook the largest one first (if the largest one plus current cooked dishes sum remains positive)
    # Otherwise we stop and return   
    '''    
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        result, current = 0, 0
        while satisfaction and satisfaction[-1] + current > 0:
            current += satisfaction.pop()
            result += current
        return result
    # @lc code=end

