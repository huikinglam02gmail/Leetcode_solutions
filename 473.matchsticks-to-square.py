#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    A repeat of Leetcode 698. Here k = 4
    '''
    @lru_cache(None)
    def dfs(self, i, state):
        stateList = [int(c) for c in state.split("_")]
        if i == len(self.Nums):
            return all([s == self.target for s in stateList])
        else:
            for l in range(self.k):
                if self.Nums[i] + stateList[l] <= self.target:
                    stateList[l] += self.Nums[i]
                    if self.dfs(i + 1, "_".join([str(j) for j in sorted(stateList)])):
                        return True
                    stateList[l] -= self.Nums[i]
            return False
        
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0 or max(nums) > sum(nums) // k:
            return False
        else:
            self.target = sum(nums) // k
            self.k = k
            self.Nums = sorted(nums, reverse=True)
            return self.dfs(0, "_".join(['0']*k))

    def makesquare(self, matchsticks: List[int]) -> bool:
        return self.canPartitionKSubsets(matchsticks, 4)
        
# @lc code=end

