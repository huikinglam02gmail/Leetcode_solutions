#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    DP problem
    dp(i,j) = maximum dot product between non-empty subsequences of nums1[i:] and nums2[j:] with the same length.
    We are looking for dp(0,0)
    We can either choose to use, or skip nums1[i] and nums2[j]
    Base cases: when i, j = n1, n2, return 0 respectively
    Twist with the nonempty requirement: it would happen if max(nums1) < 0 and min(nums2) > 0 or max(nums1) > 0 and min(nums2) < 0
    For the case we just return max(nums1)*min(nums2) and min(nums1)*max(nums2) respectively   
    '''
        
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        max1, min1, max2, min2 = max(nums1), min(nums1), max(nums2), min(nums2)
        if max1 < 0 and min2 > 0:
            return max1 * min2
        if max2 < 0 and min1 > 0:
            return max2 * min1
        n1, n2 = len(nums1), len(nums2)
        dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1) ]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1]
                if nums1[i] * nums2[j] > 0:
                    dp[i][j] += nums1[i] * nums2[j]
                dp[i][j] = max(dp[i][j], dp[i + 1][j])
                dp[i][j] = max(dp[i][j], dp[i][j + 1])
        return dp[0][0]

# @lc code=end

