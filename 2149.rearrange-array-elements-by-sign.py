#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just separate into two lists
    And join them into even and odd indices
    '''
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arrs, firstIsPositive, n = [[] for i in range(2)], nums[0] > 0, len(nums)
        for num in nums:
            arrs[(num > 0) ^ firstIsPositive].append(num)
        result = []
        for i in range(n // 2):
            result.append(arrs[1 - firstIsPositive][i])
            result.append(arrs[firstIsPositive][i])
        return result
# @lc code=end

