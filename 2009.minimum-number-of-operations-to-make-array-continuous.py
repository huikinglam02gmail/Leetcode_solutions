#
# @lc app=leetcode id=2009 lang=python3
#
# [2009] Minimum Number of Operations to Make Array Continuous
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    First sort nums
    Then we ask: if nums[i] : nums[i] + n - 1 is our target, how many of the numbers are outside? Minimize it.
    Note: we need to change all duplicates (except the first appearance). So carry out the binary search in the distinct number sorted array
    '''
    def minOperations(self, nums: List[int]) -> int:
        n =  len(nums)
        nums = sorted(set(nums))
        result = float("inf")
        for num in nums:
            startIndex = bisect.bisect_left(nums, num)
            endIndex = bisect.bisect_left(nums, num + n - 1)
            if endIndex == len(nums) or nums[endIndex] != num + n - 1:
                endIndex -= 1
            result = min(result, n - (endIndex - startIndex + 1))
        return result
# @lc code=end

