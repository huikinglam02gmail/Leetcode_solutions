#
# @lc app=leetcode id=2815 lang=python3
#
# [2815] Max Pair Sum in an Array
#

# @lc code=start
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        hashTable = [[] for i in range(10)]
        for num in nums:
            numString = str(num)
            maxDigit = 0
            for c in numString:
                maxDigit = max(int(c), maxDigit)
            hashTable[maxDigit].append(num)
        result = -1
        for i in range(10):
            if len(hashTable[i]) >= 2:
                hashTable[i].sort()
                result = max(result, hashTable[i][-1] + hashTable[i][-2])
        return result
# @lc code=end

