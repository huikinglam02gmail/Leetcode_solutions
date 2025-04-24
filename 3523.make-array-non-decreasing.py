#
# @lc app=leetcode id=3523 lang=python3
#
# [3523] Make Array Non-decreasing
#

# @lc code=start
from typing import List


class Solution:
    '''
    iterate backwards and form monotonic nonincreasing stack
    '''
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for num in nums[::-1]:
            while stack and num > stack[-1]: stack.pop()
            stack.append(num)
        return len(stack)
# @lc code=end

