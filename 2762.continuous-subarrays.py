#
# @lc app=leetcode id=2762 lang=python3
#
# [2762] Continuous Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use sliding window. Also, use a hash table to keep the number: last occurring index
    When a new num comes in, loop through current keys to look for abs(key - num) > 2. Left -> max(left, lastIndex + 1)
    '''
    def continuousSubarrays(self, nums: List[int]) -> int:
        hashTable = {}
        l = 0
        result = 0
        for r in range(len(nums)):
            keysToPop = []
            for key in hashTable:
                if abs(key - nums[r]) > 2: 
                    l = max(l, hashTable[key] + 1)
                    keysToPop.append(key)
            for key in keysToPop: hashTable.pop(key)
            result += r - l + 1
            hashTable[nums[r]] = r
        return result
# @lc code=end

