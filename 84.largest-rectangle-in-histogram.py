#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    '''
    Keep a monotonic increasing stack of height. When a shorter height comes in and we need to pop, the column at stack[-1] can form a rectangle of size heights[stack[-1]] * (i - stack[-1]). We record where is the last popped index and height of current column in the stack (Because the current column can extend up to that specified in the popped position). We add 0 before and after heights such that the result is given after looping through the whole array
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = height*(i - index)
                max_area = max(max_area, area)
            stack.append([index, heights[i]])        
        return max_area
        
# @lc code=end

