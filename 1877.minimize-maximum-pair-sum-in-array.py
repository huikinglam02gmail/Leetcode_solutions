#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort nums and get out of each end-end pairs
    '''
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        result = 0
        while i < j:
            result = max(result, nums[i] + nums[j])
            i += 1
            j -= 1
        return result
# @lc code=end

