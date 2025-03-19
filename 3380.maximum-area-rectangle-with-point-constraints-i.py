#
# @lc app=leetcode id=3380 lang=python3
#
# [3380] Maximum Area Rectangle With Point Constraints I
#

# @lc code=start
from typing import List


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        pointsSet = set()
        points.sort()
        result = 0
        for x, y in points: pointsSet.add((x, y))
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                    count = 0
                    for x, y in points:
                        if not ((x == x1 and y == y1) or (x == x1 and y == y2) or (x == x2 and y == y1) or (x == x2 and y == y2)) and x1 <= x <= x2 and y1 <= y <= y2:
                            count += 1
                    if count == 0: result = max(result, (x2 - x1) * (y2 - y1))
        return - 1 if result == 0 else result

# @lc code=end

