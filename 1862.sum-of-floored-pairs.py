#
# @lc app=leetcode id=1862 lang=python3
#
# [1862] Sum of Floored Pairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    Let's think about a simpler problem. Given nums = [1, 2, 3, 4, 6], what is the sum of floored pairs with 1 as divisor?
    The answer is 1 + 2 + 3 + 4 + 6
    How about if 2 is the divisor?
    We have 0 + 1 + 1 + 2 + 3
    We see that for each num as the divisor, we can accumulate its contribution as prefix sum. Increment can be increased at intervals of num 
    Therefore we record the occurrences of nums. Then we assign an increment array of size (max(nums) + 1). For each key, we increment by num, the number of occurrence of num, To get the final contribution, we perform prefix sum, and finally multiply the number of occurrences of each key.
    '''
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        hashTable = {}
        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1
        
        increment = [0] * (max(hashTable.keys()))
        for key in hashTable.keys():
            for j in range(key, len(increment) + 1, key):
                increment[j - 1] += hashTable[key]
        prefixSum = [0]
        for inc in increment:
            prefixSum.append(prefixSum[-1] + inc)
        result = 0
        MOD = pow(10, 9) + 7
        for key in hashTable.keys():
            result += hashTable[key] * prefixSum[key]
            result %= MOD
        return result
# @lc code=end

