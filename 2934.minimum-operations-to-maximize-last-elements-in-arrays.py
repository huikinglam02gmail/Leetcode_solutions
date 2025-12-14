#
# @lc app=leetcode id=2934 lang=python3
#
# [2934] Minimum Operations to Maximize Last Elements in Arrays
#

# @lc code=start
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        res1 = self.steps(nums1, nums2)
        nums2[-1], nums1[-1] = nums1[-1], nums2[-1]
        res2 = 1 + self.steps(nums1, nums2)
        res = min(res1, res2)
        return res if res != float("inf") else -1

    def steps(self, nums1, nums2):
        result = 0
        n = len(nums1)
        for i in range(n - 1):
            if nums1[i] <= nums1[n - 1] and nums2[i]<= nums2[n - 1]:
                continue
            elif nums1[i] <= nums2[n - 1] and nums2[i] <= nums1[n - 1]:
                result += 1
            else: 
                result = float("inf")
        return result
# @lc code=end
