#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
from typing import List


class Solution:
    '''
    sliding window + hash Table
    '''
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashTable = {}
        left = 0
        result = 0
        for right, num in enumerate(nums):
            while hashTable.get(num, 0) == k:
                hashTable[nums[left]] -= 1
                left += 1
            hashTable[nums[right]] = hashTable.get(nums[right], 0) + 1
            result = max(result, right - left + 1)
        return result
        
# @lc code=end

