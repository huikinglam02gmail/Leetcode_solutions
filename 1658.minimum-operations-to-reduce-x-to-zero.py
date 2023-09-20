#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
from typing import List


class Solution:
    '''
    Find maximum middle subarray that sums to total - x
    Sliding window  
    '''
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        if total < x:
            return -1
        elif total == x:
            return n
        else:
            result, S, l = 0, 0, 0
            for r, num in enumerate(nums):
                S += num
                while l < r and S > total - x:
                    S -= nums[l]
                    l += 1
                if S == total - x:
                    result = max(result, r - l + 1)
            return -1 if result == 0 else n - result
# @lc code=end

