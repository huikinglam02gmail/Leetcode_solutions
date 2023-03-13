#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    count all the nums occurrence. For each num and k - num, if k != 2* num, we can get min(count(num), count(k - num)). Else, we get count(num) // 2 * 2. Divide final answer by 2
    '''
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashTable = {}
        for num in nums:
            if num not in hashTable:
                hashTable[num] = 0
            hashTable[num] += 1
        result = 0
        for key, value in hashTable.items():
            if 2*key != k and k - key in hashTable:
                result += min(hashTable[key], hashTable[k - key])
            elif k == 2*key:
                result += (hashTable[key] // 2) * 2
        return result // 2
# @lc code=end

