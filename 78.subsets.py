#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    '''
    Generate the power set    
    '''
    def generate(self, numbers, k, combination):
        if k == 0:
            if combination not in self.result: self.result.append(combination)
            return
        else:
            for i in range(len(numbers)): self.generate(numbers[i+1:], k-1, combination + [numbers[i]])
    
    def combine(self, nums, k: int) -> List[List[int]]:
        self.result = []
        self.generate(nums, k, [])
        return self.result
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for i in range(1,len(nums)+1,1): results += self.combine(nums, i)
        return results
# @lc code=end

