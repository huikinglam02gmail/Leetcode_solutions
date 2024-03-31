#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each index i, consider all the subarrays from j <= i. We want the subarrays that exclude nums[j] < minK and nums[j] > maxK. Therefore we keep a record of the latest of such indices jBad. In addition, we record the last appearance of jMin: nums[jMin] = minK, and jMax: nums[jMax] = maxK. Once we have these three, we add max(0, min(jMin, jMax) - jBad) to the result
    '''
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        jMax, jMin, jBad, result = -1, -1, -1, 0
        for j, num in enumerate(nums):
            if num < minK or num > maxK:
                jBad = j
            if num == minK:
                jMin = j
            if num == maxK:
                jMax = j
            result += max(0, min(jMin, jMax) - jBad)
        return result


        
# @lc code=end
