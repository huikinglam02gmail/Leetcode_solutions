#
# @lc app=leetcode id=2952 lang=python3
#
# [2952] Minimum Number of Coins to be Added
#

# @lc code=start
from typing import List


class Solution:
    '''
    same question as 330.
    '''
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        return self.minPatches(sorted(coins), target)
        
    def minPatches(self, nums: List[int], n: int) -> int:
        reach = 0
        count = 0
        index = 0
        while reach < n:
            if index < len(nums) and nums[index] <= reach + 1:
                reach += nums[index]
                index += 1
            else:
                count += 1
                reach += reach + 1
        return count
# @lc code=end

