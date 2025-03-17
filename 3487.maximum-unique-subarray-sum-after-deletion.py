#
# @lc app=leetcode id=3487 lang=python3
#
# [3487] Maximum Unique Subarray Sum After Deletion
#

# @lc code=start
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        hashTable = {}
        numOfPositives = 0
        numOfZeroes = 0
        numOfNegatives = 0
        for num in nums: 
            if num > 0: numOfPositives += 1
            elif num == 0: numOfZeroes += 1
            else: numOfNegatives += 1
            hashTable[num] = hashTable.get(num, 0) + 1
        result = 0
        if numOfPositives > 0:
            for num in hashTable:
                if num > 0: result += num
        elif numOfZeroes == 0 and numOfNegatives > 0:
            result += max(hashTable.keys())
        return result
    
# @lc code=end

