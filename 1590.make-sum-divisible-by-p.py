#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
from typing import List


class Solution:
    '''
    let's calculate the prefix sum
    we are looking for subarrays in which (Total - (PS[j] - PS[i])) % p == 0
    PS[j] % p == (Total + PS[i]) % p = Total % p + PS[i] % p
    Therefore we look for PS[i] % p = PS[j] % p - Total % p (if positive) or PS[j] % p - Total % p + p
    '''
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        result = len(nums)
        if total % p == 0: return 0
        elif total < p: return -1
        
        prefix = [0]
        hashTable = {}
        hashTable[0] = -1        
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + num)
            keyToLookFor = (p + prefix[-1] % p - total % p) % p 
            if keyToLookFor in hashTable: result = min(result, i - hashTable[keyToLookFor])
            hashTable[prefix[-1] % p] = i
        if result < len(nums): return result
        else: return -1


# @lc code=end

