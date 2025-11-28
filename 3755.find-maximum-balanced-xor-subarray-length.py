#
# @lc app=leetcode id=3755 lang=python3
#
# [3755] Find Maximum Balanced XOR Subarray Length
#
from typing import List

# @lc code=start
class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        data = {}
        data[0] = {}
        data[0][0] = -1
        prefix = 0
        oddCount = 0
        result = 0
        for i, num in enumerate(nums):
            prefix ^= num
            if num & 1: oddCount += 1
            mark =  i + 1 - 2 * oddCount
            if prefix in data and mark in data[prefix]:
                result = max(result, i - data[prefix][mark])
            if prefix not in data:
                data[prefix] = {}
            if mark not in data[prefix]:
                data[prefix][mark] = i        
        return result
# @lc code=end

