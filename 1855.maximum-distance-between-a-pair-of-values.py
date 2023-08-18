#
# @lc app=leetcode id=1855 lang=python3
#
# [1855] Maximum Distance Between a Pair of Values
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Notice nums1 and nums2 are already sorted, but in reverse order
    If we reverse both nums1 and nums2, take n1 = len(nums1) and n2 = len(nums2), the question becomes:
    For each index i1 = n1 - 1 to 0 in nums1, bisect_left for nums1[i1]  inside nums2
    If the index >= n2 - n1 + i1 + 1, we do not find a match
    If we find index < n2 - n1 + i1 + 1, the maximum distance for the current pair is n2 - n1 - index + i1
    '''
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.reverse()
        nums2.reverse()
        result = 0
        n1, n2 = len(nums1), len(nums2)
        for i1 in range(n1 - 1, -1, -1):
            ind = bisect.bisect_left(nums2, nums1[i1])
            if ind < n2 - n1 + i1 + 1:
                result = max(result, n2 - n1 + i1 - ind)
        return result
# @lc code=end

