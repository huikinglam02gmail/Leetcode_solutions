#
# @lc app=leetcode id=2150 lang=python3
#
# [2150] Find All Lonely Numbers in the Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort and consider
    '''
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if (i == 0 or nums[i] - nums[i - 1] > 1) and (i == n - 1 or nums[i + 1] - nums[i] > 1): result.append(nums[i])
        return result
        
# @lc code=end

