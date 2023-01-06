#
# @lc app=leetcode id=1591 lang=python3
#
# [1591] Strange Printer II
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # First we build the expected rectangles of different colors
    # This is given by the expected top left and bottom right corners
    # We can find that by finding the maximum and minimum of x and y coordinates respectively
    # After that, we collect all the colors and put into a queue.
    # For each color, we examine if we can collect the whole rectangle
    # If so, we convert the rectangle into wildcard = 0
    # We can check the queue before and after going through each color and compare if it got shortened
    # If so, return false
    
    def formCompleteRectangle(self, xmin, xmax, ymin, ymax, color):
        for j in range(xmin, xmax+1):
            for k in range(ymin, ymax+1):
                if self.A[j][k] != 0 and self.A[j][k] != color:
                    return False
        for j in range(xmin, xmax+1):
            for k in range(ymin, ymax+1):
                self.A[j][k] = 0
        return True
    
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = {}
        for i in range(m):
            for j in range(n):
                if targetGrid[i][j] not in colors:
                    colors[targetGrid[i][j]] = [m, n, 0, 0]
                colors[targetGrid[i][j]][0] = min(colors[targetGrid[i][j]][0],i)
                colors[targetGrid[i][j]][1] = min(colors[targetGrid[i][j]][1],j)
                colors[targetGrid[i][j]][2] = max(colors[targetGrid[i][j]][2],i)
                colors[targetGrid[i][j]][3] = max(colors[targetGrid[i][j]][3],j)

        self.A = targetGrid
        colorKeys = list(colors.keys())
        dq = deque()
        for key in colorKeys:
            dq.append(key)
        while dq:
            oldLength = len(dq)
            for i in range(oldLength):
                color = dq.popleft()
                if not self.formCompleteRectangle(colors[color][0], colors[color][2],colors[color][1], colors[color][3], color):
                    dq.append(color)
            if len(dq) == oldLength:
                return False
        return True
# @lc code=end
