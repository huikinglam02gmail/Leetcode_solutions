#
# @lc app=leetcode id=1964 lang=python3
#
# [1964] Find the Longest Valid Obstacle Course at Each Position
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Use LIS monotonic stack method
    '''
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stack = []
        result = []
        for o in obstacles:
            i = bisect.bisect_right(stack, o)
            result.append(i + 1)
            if i == len(stack):
                stack.append(o)
            else:
                stack[i] = o
        return result

# @lc code=end

