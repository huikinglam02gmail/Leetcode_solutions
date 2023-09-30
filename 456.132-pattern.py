#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
from typing import List


class Solution:
    '''
    generate a monotonic decreasing stack of [num, minimum before seeing num]. When a new num comes, we first record the minimum so far including itself. Then it pop from the stack if the top is smaller than or equal to itself, so the current element acts as a potential second element. If we see the last element is larger than num and its minimum before it is smaller than num, we found the answer.
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            thisMin = num
            if stack:
                thisMin = min(thisMin, stack[-1][1])
            while stack and num >= stack[-1][0]:
                stack.pop()
            if len(stack) > 0 and stack[-1][1] < num:
                return True    
            stack.append([num, thisMin])           
        return False
                
# @lc code=end

