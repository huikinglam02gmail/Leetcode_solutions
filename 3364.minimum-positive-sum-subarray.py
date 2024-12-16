#
# @lc app=leetcode id=3364 lang=python3
#
# [3364] Minimum Positive Sum Subarray 
#

# @lc code=start
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefix = [0]
        for num in nums: prefix.append(prefix[-1] + num)
        result = float("inf")
        for i in range(l, r + 1):
            for j in range(len(prefix) - i):
                S = prefix[j + i] - prefix[j]
                if S > 0: result = min(result, S)
        return -1 if result == float("inf") else result
# @lc code=end

