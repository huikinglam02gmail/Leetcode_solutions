#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use string separated by _ to represent the solution
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = [set() for i in range(target + 1)]
        result[0].add("")
        for cand in candidates:
            for i in range(target, cand - 1, -1):
                for s in result[i - cand]:
                    result[i].add(s + "_" + str(cand))
        return [[int(num) for num in s.split("_")[1:]] for s in result[target]]

# @lc code=end

