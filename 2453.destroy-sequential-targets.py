#
# @lc app=leetcode id=2453 lang=python3
#
# [2453] Destroy Sequential Targets
#

# @lc code=start
from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] % space not in hashTable: hashTable[nums[i] % space] = [0, float("inf")]
            hashTable[nums[i] % space][0] += 1
            hashTable[nums[i] % space][1] = min(hashTable[nums[i] % space][1], nums[i])
        
        maxCount = 0
        result = float("inf")
        for count, smallest in hashTable.values():
            if count > maxCount:
                maxCount = count
                result = smallest
            elif count == maxCount and smallest < result:
                result = smallest
        return result
# @lc code=end

