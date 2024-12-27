#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    Instead of finding the bad pairs, it's easier to find how many good pairs are there
    Definition of good pairs: i - nums[i] == j - nums[j]
    '''
    def countBadPairs(self, nums: List[int]) -> int:
        goodPairs = {}
        good = 0
        for i in range(len(nums)):
            currentKey = i - nums[i]
            good += goodPairs.get(currentKey, 0)
            goodPairs[currentKey] = goodPairs.get(currentKey, 0) + 1
        return (len(nums) - 1) * len(nums) // 2 - good
# @lc code=end

