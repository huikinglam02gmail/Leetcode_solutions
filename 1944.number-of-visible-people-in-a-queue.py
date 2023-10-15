#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
from typing import List


class Solution:
    '''
    Maintain a monotonic decreasing stack. The answer to each index is composed of two parts:
    1. How many elements smaller than heights[i] at the right of it, which should increase monotonically.
    2. What there is a right element larger than itself 
    '''
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
                result[i] += 1
            if stack:
                result[i] += 1
            stack.append(i)
        return result
# @lc code=end

