#
# @lc app=leetcode id=3314 lang=python3
#
# [3314] Construct the Minimum Bitwise Array I
#

# @lc code=start
from typing import List


class Solution:
    '''
    2 <= nums[i] <= 1000
    we can brute force all possible pairs below max(nums) and store in a hashTable
    '''
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        hashTable = {}
        for i in range(1000, -1, -1):
            hashTable[i | (i + 1)] = i
        return [hashTable.get(num, -1) for num in nums]
        
# @lc code=end

