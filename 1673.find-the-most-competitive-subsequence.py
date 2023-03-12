#
# @lc app=leetcode id=1673 lang=python3
#
# [1673] Find the Most Competitive Subsequence
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use monotonic increasing stack to tackle the problem. Whenever the available elements left is more than k, we are free to remove from the back of stack if we can get lexicographically smaller stack
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

