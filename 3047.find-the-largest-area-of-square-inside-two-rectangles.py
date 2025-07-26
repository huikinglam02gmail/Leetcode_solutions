#
# @lc app=leetcode id=3047 lang=python3
#
# [3047] Find the Largest Area of Square Inside Two Rectangles
#

# @lc code=start
from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        data = []
        for i in range(len(bottomLeft)):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]
            data.append([x1, y1, x2, y2])
        data.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
        maxArea = 0
        for i in range(len(data) - 1):
            x1, y1, x2, y2 = data[i]
            for j in range(i + 1, len(data)):
                x3, y3, x4, y4 = data[j]
                if not x1 <= x3 <= x2: continue
                if max(y1, y3) > min(y2, y4): continue
                side = min(min(x2, x4) - x3, min(y2, y4) - max(y1, y3))
                maxArea = max(maxArea, side * side)
        return maxArea
# @lc code=end

