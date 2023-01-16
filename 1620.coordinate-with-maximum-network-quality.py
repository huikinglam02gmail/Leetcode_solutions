#
# @lc app=leetcode id=1620 lang=python3
#
# [1620] Coordinate With Maximum Network Quality
#

# @lc code=start
import math
from typing import List


class Solution:
    # 1 <= towers.length <= 50
    # 0 <= xi, yi, qi <= 50
    # So just brute force
    
    def euclidean(self, x1, y1, x2, y2):
        return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        quality = [[0 for j in range(51)] for i in range(51)]
        for x, y, q in towers:
            for i in range(51):
                for j in range(51):
                    d = self.euclidean(i, j, x, y)
                    if d <= radius:
                        quality[i][j] += math.floor(q / (1+d))
        
        x, y, qMax = 0, 0, 0
        for i in range(51):
            for j in range(51):
                if quality[i][j] > qMax:
                    qMax = quality[i][j]
                    x, y = i, j
        return [x, y]
# @lc code=end
