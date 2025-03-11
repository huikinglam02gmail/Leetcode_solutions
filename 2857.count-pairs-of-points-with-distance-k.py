#
# @lc app=leetcode id=2857 lang=python3
#
# [2857] Count Pairs of Points With Distance k
#

# @lc code=start
from typing import List


class Solution:
    '''
    0 <= k <= 100
    so scan x + y = k
    x = x1 ^ x2 and y = y1 ^ y2 = k - x
    For each x1, look for x2 = x ^ x1 and y2 = (k - x) ^y1
    '''
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        coord = {}
        for x, y in coordinates: coord[(x, y)] = coord.get((x, y), 0) + 1
        result = 0
        for j in range(k + 1):
            for x, y in coord.keys():
                if (j ^ x, (k - j) ^ y) in coord:
                    if x == j ^ x and y == (k - j) ^ y: result += coord[(x, y)] * (coord[(x, y)] - 1)
                    else: result += coord[(x, y)] * coord[(j ^ x, (k - j) ^ y)]
        return result // 2
        
# @lc code=end

