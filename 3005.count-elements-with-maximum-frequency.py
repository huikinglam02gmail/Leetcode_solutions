#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashTable = {}
        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1
        maxOccur = 0
        result = 0
        for k, v in hashTable.items():
            if v > maxOccur: 
                maxOccur = v
                result = 0
            if v == maxOccur:
                result += v
        return result
        
# @lc code=end

