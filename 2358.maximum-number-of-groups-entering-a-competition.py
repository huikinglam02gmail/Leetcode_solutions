#
# @lc app=leetcode id=2358 lang=python3
#
# [2358] Maximum Number of Groups Entering a Competition
#

# @lc code=start
from typing import List


class Solution:
    '''
    number of groups formed = ans
    n >= ans * (ans + 1) // 2
    '''
    def maximumGroups(self, grades: List[int]) -> int:
        if len(grades) == 1: return 1
        l, r = 1, len(grades)
        while l < r:
            mid = l + (r - l) // 2
            if mid * (mid + 1) // 2 <= len(grades):
                l = mid + 1
            else:
                r = mid
        return l - 1
        
# @lc code=end

