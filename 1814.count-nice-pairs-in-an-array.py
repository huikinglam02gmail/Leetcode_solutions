#
# @lc app=leetcode id=1814 lang=python3
#
# [1814] Count Nice Pairs in an Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    First prepare the second array rev(nums)
    Then given the condition nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    So we just maintain this difference and maintain a set
    '''
    def countNicePairs(self, nums: List[int]) -> int:
        hashTable = {}
        result, MOD = 0, pow(10, 9) + 7
        for i, num in enumerate(nums):
            diff = num - int(str(num)[::-1])
            hashTable[diff] = hashTable.get(diff, set())
            hashTable[diff].add(i)
        for v in hashTable.values():
            result += len(v) * (len(v) - 1) // 2
            result %= MOD
        return result
        
# @lc code=end

