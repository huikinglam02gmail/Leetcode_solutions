#
# @lc app=leetcode id=2216 lang=python3
#
# [2216] Minimum Deletions to Make Array Beautiful
#

# @lc code=start
from typing import List


class Solution:
    '''
    Simulate the process with a stack
    '''
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        result = 0
        for i in range(len(nums)):
            if not (stack and len(stack) % 2 > 0 and nums[stack[-1]] == nums[i]): stack.append(i)
            else: result += 1
        if len(stack) % 2 > 0: result += 1
        return result
        
# @lc code=end

