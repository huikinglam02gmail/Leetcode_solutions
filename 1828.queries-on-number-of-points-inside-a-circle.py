#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= points.length <= 500
    1 <= queries.length <= 500
    So in principle we can find if dist(points[i], queriespoint) <= queriesDistance and this will pass 
    '''
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result  = []
        for x, y, r in queries:
            count = 0
            for x1, y1 in points:
                if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
                    count += 1
            result.append(count)
        return result

# @lc code=end

