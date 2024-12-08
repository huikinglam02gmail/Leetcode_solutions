#
# @lc app=leetcode id=2592 lang=python3
#
# [2592] Maximize Greatness of an Array
#

# @lc code=start
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_indices = sorted(enumerate(nums2), key = lambda x: x[1])
        p1, p2, l1 = len(nums1)-1, len(nums1)-1, 0
        result = [-1 for i in range(len(nums1))]
        while p1 >= l1:
            if nums1[p1] > nums2_indices[p2][1]:
                result[nums2_indices[p2][0]] = nums1[p1]
                p1 -= 1
            else:
                result[nums2_indices[p2][0]] = nums1[l1]
                l1 += 1
            p2 -= 1
        return result
    
    def maximizeGreatness(self, nums: List[int]) -> int:
        perm = self.advantageCount(nums, nums)
        result = 0
        for p, n in zip(perm, nums):
            if p > n: result += 1
        return result
# @lc code=end

