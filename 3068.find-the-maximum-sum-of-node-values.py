#
# @lc app=leetcode id=3068 lang=python3
#
# [3068] Find the Maximum Sum of Node Values
#

# @lc code=start
from typing import List


class Solution:
    '''
    As the graph is a tree, we can always flip even number of nodes (no need to care about the edges) to get a larger sum.
    That is count(num ^ k > num for num in nums) is even, we can return the maximum sum possible
    For the case in which this count is odd, we have to reduce the maxSum by min(abs(num ^ k - num)), which points to the node in which num is closest to num ^ k. For example, in example 2 becomes nums = [7, 3], k = 7, maxSum is 7 + 4 = 11, and count = 1. As count is odd, the maxSum has included an flip that violated the rule. We can choose the one which induced the least change, which is flip of 3 to 4. 
    '''
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        count = 0
        maxSum = 0
        sacrifice = float("inf")
        for num in nums:
            if num ^ k > num: count += 1
            sacrifice = min(sacrifice, abs(num ^ k - num))
            maxSum += max(num, num ^ k)
        if count % 2: maxSum -= sacrifice
        return maxSum
        
# @lc code=end

