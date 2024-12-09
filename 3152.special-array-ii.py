#
# @lc app=leetcode id=3152 lang=python3
#
# [3152] Special Array II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use prefix Sum: prefix[i] = 1 if nums[i] % 2 != nums[i - 1] % 2, else 0
    '''
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for i in range(1, len(nums), 1): prefix.append(prefix[-1] + abs(nums[i] % 2 - nums[i - 1] % 2))
        result = []
        for f, t in queries: result.append(prefix[t] - prefix[f] == t - f)
        return result
        
# @lc code=end

