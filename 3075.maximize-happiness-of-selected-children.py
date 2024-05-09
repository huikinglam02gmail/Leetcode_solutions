#
# @lc app=leetcode id=3075 lang=python3
#
# [3075] Maximize Happiness of Selected Children
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort, go backwards and keep track of how many has already been added
    '''
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        n = len(happiness)
        result = 0
        for i in range(n - 1, n - k - 1, -1): result += max(0, happiness[i] - (n - 1 - i))
        return result
# @lc code=end

