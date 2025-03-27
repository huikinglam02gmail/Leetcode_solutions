#
# @lc app=leetcode id=2780 lang=python3
#
# [2780] Minimum Index of a Valid Split
#

# @lc code=start
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        totalHashTable = {}
        for num in nums: totalHashTable[num] = totalHashTable.get(num, 0) + 1
        leftHashTable = {}
        for i in range(len(nums)):
            leftHashTable[nums[i]] = leftHashTable.get(nums[i], 0) + 1
            if leftHashTable[nums[i]] > (i + 1) // 2 and (totalHashTable[nums[i]] - leftHashTable[nums[i]]) > (len(nums) - 1 - i) // 2: return i
        return -1
# @lc code=end

