#
# @lc app=leetcode id=1685 lang=python3
#
# [1685] Sum of Absolute Differences in a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    For nums[i], smaller number nums[j] would give nums[i] - nums[j] and larger number nums[k] would give nums[k] - nums[i]. So what we need is sum of (i*nums[i] -  sum(nums[:i])) + (sum(nums[i+1:]) - (n - i)*nums[i]). The sum can be handled by prefix sum
    '''
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
# @lc code=end

