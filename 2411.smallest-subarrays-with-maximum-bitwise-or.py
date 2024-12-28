#
# @lc app=leetcode id=2411 lang=python3
#
# [2411] Smallest Subarrays With Maximum Bitwise OR
#

# @lc code=start
from typing import List


class Solution:
    '''
    0 <= nums[i] <= 10^9
    The largest bitwise OR is given by ORing all the numbers after it.
    Therefore we use a hashTable counting all the set bits.
    Then we use a sliding window to keep remove previous index
    '''
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        hashTable = {}
        bitMask = 0
        for num in nums:
            for i in range(31):
                if num & (1 << i) > 0: 
                    hashTable[i] = hashTable.get(i, 0) + 1
                    bitMask |= (1 << i)
        maxOR = []
        for i in range(len(nums)):
            if i > 0:
                for j in range(31):
                    if nums[i - 1] & (1 << j) > 0:
                        hashTable[j] = hashTable.get(j, 0) - 1
                        if hashTable[j] == 0: 
                            hashTable.pop(j)
                            bitMask ^= (1 << j)
            maxOR.append(bitMask)
        
        r = 0
        result = []
        bitMask = 0
        hashTable =  {}
        for l in range(len(nums)):
            if l > 0:
                for j in range(31):
                    if nums[l - 1] & (1 << j) > 0:
                        hashTable[j] = hashTable.get(j, 0) - 1
                        if hashTable[j] == 0: 
                            hashTable.pop(j)
                            bitMask ^= (1 << j)
            while r < len(nums) and bitMask != maxOR[l]:
                for j in range(31):
                    if nums[r] & (1 << j) > 0: 
                        hashTable[j] = hashTable.get(j, 0) + 1
                        bitMask |= (1 << j)
                r += 1
            result.append(max(r - l, 1))
        return result
        
# @lc code=end
