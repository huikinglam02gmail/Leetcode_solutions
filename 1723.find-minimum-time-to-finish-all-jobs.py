#
# @lc app=leetcode id=1723 lang=python3
#
# [1723] Find Minimum Time to Finish All Jobs
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    Very similar problem to Leetcode 698 Partition to K Equal Sum Subsets
    Again we sort the jobs from large to small and states from small to large

    Key difference: we do not have target here. Instead the DFS function should return the minimum time to finish instad of whether can form target.
    '''
    @lru_cache(None)
    def dfs(self, i, state):
        stateList = [int(c) for c in state.split("_")]
        if i == len(self.Nums):
            return max(stateList)
        else:
            result = float('Inf')
            for l in range(self.k):
                stateList[l] += self.Nums[i]
                if max(stateList) < result:
                    result = min(result, self.dfs(i + 1, "_".join([str(j) for j in sorted(stateList)])))
                stateList[l] -= self.Nums[i]
            return result

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.Nums = sorted(jobs, reverse=True)
        self.k = k
        return self.dfs(0, "_".join(['0']*k))
        
# @lc code=end
