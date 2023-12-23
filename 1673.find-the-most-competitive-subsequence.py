#
# @lc app=leetcode id=1673 lang=python3
#
# [1673] Find the Most Competitive Subsequence
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use monotonic increasing stack to tackle the problem.
    When the incoming number is smaller than stack[-1], we can pop from the stack if we can ensure we replace stack[-1] with nums[i:], we have enough elements to get to length of k
    '''
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while stack and num < stack[-1] and n - i + len(stack) - 1 >= k:
                stack.pop()
            stack.append(num)
        return stack[:k]
        
# @lc code=end

