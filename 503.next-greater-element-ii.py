#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use a monotonic decreasing stack to find the next larger num.
    First concatenate two nums. First initialize the every element of result to be -1. Then whenever we see an incoming element to be larger than the stack top, the stack top's next greater element is in the incoming element
    '''
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums2 = nums + nums
        next_greater = [-1 for i in range(len(nums2))]
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                next_greater[stack.pop()] = nums2[i]
            stack.append(i)
        return next_greater[:len(nums)]
# @lc code=end

