#
# @lc app=leetcode id=1879 lang=python3
#
# [1879] Minimum XOR Sum of Two Arrays
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    1 <= n <= 14
    So can try brute force the solution, supplemented by DP
    dp[i][mask] = minimum XOR sum if nums1[i:] is left, with mask representing the elements are used.
    dp[i][mask] = min(nums1[i]^nums2[j] + dp[i + 1][mask ^ (1 << j)]), given mask & (1 << j) = 0
    '''
    @lru_cache(None)
    def dp(self, i, mask):
        if i == len(self.nums1):
            return 0
        else:
            result = float("Inf")
            for j in range(len(self.nums1)):
                if (mask & (1 << j)) == 0:
                    result = min(result, (self.nums1[i] ^ self.nums2[j]) + self.dp(i + 1, mask ^ (1 << j)))
            return result
        
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1 = nums1
        self.nums2 = nums2
        return self.dp(0, 0)
        
# @lc code=end

