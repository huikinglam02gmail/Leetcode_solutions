#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    We first sort [nums1, nums2] reversely with larger nums2 considered first
    Then we maintain a min heap of nums1 such that when len(heap) > k, we pop out the minimum number inside nums1. Therefore we considered the min(nums2) in the k-subsequence (ensured by sorting) and the maximum possible nums1 sum (ensured by heap)
    '''
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        data = sorted(zip(nums1, nums2), key = lambda x: -x[1])
        heap, S, result = [], 0, 0
        for a, b in data:
            S += a
            heapq.heappush(heap, a)
            if len(heap) > k: S -= heapq.heappop(heap)
            if len(heap) == k: result = max(result, b * S)
        return result
# @lc code=end

