#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashTable = {}
        n = len(nums)
        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1
        result = []
        for k, v in hashTable.items():
            if v > n // 3:
                result.append(k)
        return result
        
# @lc code=end

