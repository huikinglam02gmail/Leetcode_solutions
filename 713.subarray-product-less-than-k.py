#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
# sliding windows approach
from typing import List


class Solution:
    '''
    Try for every index, expand the right index until product >= k
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        left = 0
        result = 0
        product = 1
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[left]
                left += 1
            result += right - left + 1
        return result
# @lc code=end

