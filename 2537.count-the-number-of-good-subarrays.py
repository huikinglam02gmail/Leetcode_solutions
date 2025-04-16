#
# @lc app=leetcode id=2537 lang=python3
#
# [2537] Count the Number of Good Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        hashTable = {}
        result = 0
        numPairs = 0
        l = 0
        for num in nums:
            if num not in hashTable: hashTable[num] = 0
            else: numPairs += hashTable[num]
            hashTable[num] += 1    
            while numPairs >= k:
                hashTable[nums[l]] -= 1
                numPairs -= hashTable[nums[l]]
                l += 1
            result += l
        return result
            
        
# @lc code=end

