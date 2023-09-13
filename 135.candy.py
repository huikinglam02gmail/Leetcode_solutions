#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
from typing import List


class Solution:
    '''
    Scan left to right then right to left
    '''
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1 for i in range(n)]
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i] and result[i + 1] <= result[i]:
                result[i + 1] = result[i] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i-1] and result[i] >= result[i - 1]:
                result[i - 1] = result[i] + 1
        return sum(result)
# @lc code=end

