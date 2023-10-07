#
# @lc app=leetcode id=1936 lang=python3
#
# [1936] Add Minimum Number of Rungs
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    We start with height = 0, and index = - 1
    Then we bisect_right for height + dist = ind
    If ind - 1 > "index", that means we dist can reach us to ind - 1. so index = ind - 1, height = rungs[index]
    else, dist cannot reach us there. add (rungs[ind] - height) // dist  to result. assign index = ind and height = rungs[index]
    '''
    def insertRungs(self, diff, dist):
        result = diff // dist
        if diff % dist == 0:
            result -= 1
        return result

    def addRungs(self, rungs: List[int], dist: int) -> int:
        h, i, n, result = 0, -1, len(rungs), 0
        while i < n - 1:
            ind = bisect.bisect_right(rungs, h + dist)
            if ind - 1 > i:
                i = ind - 1                
            else:
                i = ind
                result += self.insertRungs(rungs[i] - h, dist)
            h = rungs[i]
        diff = rungs[-1] - h
        if diff > 0:
            result += self.insertRungs(diff, dist)
        return result
# @lc code=end
