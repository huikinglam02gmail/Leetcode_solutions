#
# @lc app=leetcode id=2576 lang=python3
#
# [2576] Find the Maximum Number of Marked Indices
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    The best case is there's 1 to 1 matching between sorted num[i] and nums[i + n // 2]. Use two pointers
    '''
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        j = len(nums) // 2
        result = 0
        for i in range(len(nums) // 2):
            while j < len(nums) and 2 * nums[i] > nums[j]: j += 1
            if j < len(nums) and 2 * nums[i] <= nums[j]:
                result += 2
                j += 1
        return result
# @lc code=end

