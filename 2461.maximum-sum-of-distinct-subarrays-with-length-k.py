#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hashTable = {}
        result = 0
        S = 0
        for i in range(len(nums)):
            if i >= k:
                S -= nums[i - k]
                hashTable[nums[i - k]] -= 1
                if hashTable[nums[i - k]] == 0: hashTable.pop(nums[i - k])
            S += nums[i]
            hashTable[nums[i]] = hashTable.get(nums[i], 0) + 1
            if i >= k - 1 and len(hashTable) == k: result = max(result, S)
        return result
# @lc code=end

