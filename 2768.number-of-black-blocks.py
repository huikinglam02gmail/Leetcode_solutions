#
# @lc app=leetcode id=2768 lang=python3
#
# [2768] Number of Black Blocks
#

# @lc code=start
from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        coordMap = {}
        for x, y in coordinates:
            if (x, y) not in coordMap: coordMap[(x, y)] = 0
            coordMap[(x, y)] += 1
            if 0 <= x < m and 0 <= y - 1 < n: 
                if (x, y - 1) not in coordMap: coordMap[(x, y - 1)] = 0
                coordMap[(x, y - 1)] += 1
            if 0 <= x - 1 < m and 0 <= y < n: 
                if (x - 1, y) not in coordMap: coordMap[(x - 1, y)] = 0
                coordMap[(x - 1, y)] += 1
            if 0 <= x - 1 < m and 0 <= y - 1 < n: 
                if (x - 1, y - 1) not in coordMap: coordMap[(x - 1, y - 1)] = 0
                coordMap[(x - 1, y - 1)] += 1
        result = [0] * 5
        count = 0
        for x, y in coordMap:
            if 0 <= x < m - 1 and 0 <= y < n - 1:
                result[coordMap[(x, y)]] += 1
                count += 1
        result[0] = (m - 1) * (n - 1) - count
        return result
# @lc code=end
