#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
from typing import List

class Solution:
    def dfs(self, nums, combination):
        if len(combination) >= 2 and tuple(combination) not in self.result:
            self.result.add(tuple(combination))
        for i in range(len(nums)):
            if not combination or nums[i] >= combination[-1]:
                self.dfs(nums[i+1:], combination + [nums[i]])

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        self.dfs(nums,[])
        return list(self.result)
        
# @lc code=end

