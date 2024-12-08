#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
from typing import List


class Solution:
    '''
    Greedy algorithm:
    Sort both
    go from high to low. If num1 high is smaller than num2 high, use num1 lowest to match against it.    
    '''
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
# @lc code=end

