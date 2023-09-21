#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    To achieve  O(log (m+n)), we notice the folllowing:
    1. if (m + n) % 2 == 0: the median is (nums[(m + n) // 2 - 1] + nums[(m + n) // 2]) / 2; if (m + n) % 2 == 1: the median is nums[(m + n) // 2]
    2. There are (m + n) // 2 numbers left and right of the median
    3. The question now is: suppose we take first x elements from nums1 and first (m + n) // 2 - x elements from nums2 to form the left (0 <= x < len(nums1)), How can we make sure it's forming a valid cut:
    4. The key is nums1[x] >= nums2[(m + n) // 2 - x - 1] and nums1[x - 1] <= nums2[(m + n) // 2 - x]
    5. If we see nums1[x] < nums2[(m + n) // 2 - x - 1], it means we should take more from nums1. Set l = x + 1
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, m
        while l < r:
            x = l + (r - l) // 2
            if (x < m and nums1[x] < nums2[(m + n) // 2 - x - 1]):
                l = x + 1
            else:
                r = x
        if (m + n) % 2 == 1:
            if l < m:
                return min(nums1[l], nums2[(m + n) // 2 - l])
            else:
                return nums2[(m + n) // 2 - l]
        else:
            left1Lim = - float("inf")
            left2Lim = - float("inf")
            right1Lim = float("inf")
            right2Lim = float("inf")
            if l > 0:
                left1Lim = nums1[l - 1]
            if (m + n) // 2 - l > 0:
                left2Lim = nums2[(m + n) // 2 - l - 1]
            if l < m:
                right1Lim = nums1[l]
            if (m + n) // 2 - l < n:
                right2Lim = nums2[(m + n) // 2 - l]
            print(left1Lim, left2Lim, right1Lim, right2Lim)
            return (max(left1Lim, left2Lim) + min(right1Lim, right2Lim)) / 2
 
# @lc code=end

