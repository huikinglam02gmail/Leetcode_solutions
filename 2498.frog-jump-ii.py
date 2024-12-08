#
# @lc app=leetcode id=2498 lang=python3
#
# [2498] Frog Jump II
#

# @lc code=start
from typing import List


class Solution:
    '''
    The optimal choice is:
    1. Forward: stones[0] -> stones[2] -> ... -> stones[n - 3] or stones[n - 2]-> stones[n - 1]
    2. Bakcward: stones[n - 1] -> stones[n - 3] -> ... -> stones[1] -> stones[0]
    '''
    def maxJump(self, stones: List[int]) -> int:
        result = stones[1] - stones[0]
        for i in range(2, len(stones)): result = max(result, stones[i] - stones[i - 2])
        return result
# @lc code=end

