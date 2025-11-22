#
# @lc app=leetcode id=2871 lang=python3
#
# [2871] Split Array Into Maximum Number of Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    Remember, total AND of the entire array is the minimum possible AND for any subarray.
    There are two cases to consider:
    1. The total AND of the entire array is non-zero. In this case, we can only have one subarray (the entire array itself).
    2. The total AND of the entire array is zero. In this case, we can split the array into multiple subarrays, each having an AND of zero.
       We can achieve this by making a new subarray every time we encounter a prefix with an AND of zero.
    '''
    def maxSubarrays(self, nums: List[int]) -> int:
        totalAnd = nums[0]
        for num in nums[1:]:
            totalAnd &= num
        if totalAnd != 0: return 1
        count = 0
        totalAnd = nums[0]
        for num in nums[1:]:
            if totalAnd == 0:
                count += 1
                totalAnd = num
            else:
                totalAnd &= num
        if totalAnd == 0:
            count += 1
        return count
# @lc code=end

