#
# @lc app=leetcode id=1818 lang=python3
#
# [1818] Minimum Absolute Sum Difference
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    We can only replace numbers on nums1. The number to look for is the number in nums1 just smaller than and above nums2[i]
    '''
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        result = sum([abs(num1 - num2) for num1, num2 in zip(nums1, nums2)])
        MOD = pow(10, 9) + 7
        nums1Sorted = sorted(nums1)
        maxGain = 0
        for i, num in enumerate(nums2):
            indLeft = bisect.bisect_left(nums1Sorted, num)
            gain = abs(nums1[i] - nums2[i])
            if 0 <= indLeft < len(nums1Sorted):
                gain = min(gain, abs(nums1Sorted[indLeft] - nums2[i]))
            if 0 <= indLeft - 1 < len(nums1Sorted):
                gain = min(gain, abs(nums1Sorted[indLeft - 1] - nums2[i]))
            maxGain = max(maxGain, abs(nums1[i] - nums2[i]) - gain)
        return (result - maxGain) % MOD
# @lc code=end

