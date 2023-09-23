#
# @lc app=leetcode id=1911 lang=python3
#
# [1911] Maximum Alternating Subsequence Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    We can treat this similar to 122. Best Time to Buy and Sell Stock II. Notice we will gain the max if we decrement (buy) at all local minimum and add (sell) at local maximum. The only difference is we need to sell first.
    '''
    def maxAlternatingSum(self, nums: List[int]) -> int:
        return nums[0] + sum([max(0, nums[i + 1] - nums[i]) for i in range(len(nums) - 1)])
# @lc code=end

