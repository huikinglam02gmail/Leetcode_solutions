#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        result = 0
        l = 0
        hashTable = {}
        total =  len(set(nums))
        for r in range(len(nums)):
            hashTable[nums[r]] = hashTable.get(nums[r], 0) + 1
            while len(hashTable) == total:
                hashTable[nums[l]] -= 1
                if hashTable[nums[l]] == 0: hashTable.pop(nums[l])
                l += 1
            result += l
        return result

# @lc code=end

