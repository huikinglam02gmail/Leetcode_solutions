#
# @lc app=leetcode id=2501 lang=python3
#
# [2501] Longest Square Streak in an Array
#

# @lc code=start
import math
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        hashTable = {}
        for num in nums:
            candidate = math.isqrt(num)
            if num not in hashTable:
                if candidate * candidate == num and candidate in hashTable: hashTable[num] = hashTable[candidate] + 1
                else: hashTable[num] = 1
        result = max(hashTable.values())
        if result < 2: return -1
        else: return result
# @lc code=end

