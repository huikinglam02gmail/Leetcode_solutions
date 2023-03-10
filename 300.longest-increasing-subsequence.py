#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect
from typing import List
class Solution:
    '''
    Keep a monotonic increasing stack of values
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []
        for i, num in enumerate(nums):
            if i == 0 or num > result[-1]: 
                result.append(num)
            elif num < result[-1]:
                index = bisect.bisect_left(result, num)
                result[index] = num
        return len(result)
# @lc code=end

