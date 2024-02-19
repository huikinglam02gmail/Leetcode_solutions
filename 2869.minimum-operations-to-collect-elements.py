#
# @lc app=leetcode id=2869 lang=python3
#
# [2869] Minimum Operations to Collect Elements
#

# @lc code=start
from typing import List


class Solution:
    '''
    pop the end
    use a need set to track what's still needed
    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        need = set()
        n = len(nums)
        for i in range(1, k + 1, 1): need.add(i)
        while nums and need:
            i = nums.pop()
            if i in need:
                need.remove(i)
        return n - len(nums)
# @lc code=end

