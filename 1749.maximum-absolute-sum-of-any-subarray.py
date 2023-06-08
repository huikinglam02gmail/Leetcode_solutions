#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
from typing import List


class Solution:
    '''
    -10^4 <= nums[i] <= 10^4
    if the maximum absolute sum subarray ends at nums[i]:
    if nums[i] < 0, we look for the minimum subarray ending at nums[i]
    if nums[i] > 0, we look for the maximum subarray ending at nums[i]
    So just do Kadane for maximum and minimum subarray, get max of the 2 abs of the 2 results
    '''
    def maxSubArray(self, nums: List[int]) -> int:      
        maxSoFar = - float('inf')
        maxEndingHere, n = 0, len(nums)        
        for num in nums:
            maxEndingHere += num
            maxSoFar = max(maxSoFar, maxEndingHere)
            maxEndingHere = max(0,maxEndingHere)
        return maxSoFar
    
    def minSubArray(self, nums: List[int]) -> int:      
        minSoFar =  float('inf')
        minEndingHere, n = 0, len(nums)        
        for num in nums:
            minEndingHere += num
            minSoFar = min(minSoFar, minEndingHere)
            minEndingHere = min(0,minEndingHere)
        return minSoFar

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(abs(self.maxSubArray(nums)), abs(self.minSubArray(nums)))
# @lc code=end

