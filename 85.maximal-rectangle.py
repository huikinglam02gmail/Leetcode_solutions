#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = height*(i - index)
                max_area = max(max_area, area)
            stack.append([index, heights[i]])        
        return max_area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        numbers = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                numbers[i][j] = int(matrix[i][j])
        max_area = 0
        for i in range(len(numbers)):
            if i == 0:
                row = numbers[i]
            else:
                for j in range(len(row)):
                    if numbers[i][j] == 0:
                        row[j] = 0
                    else:
                        row[j] += numbers[i][j]
            max_area = max(max_area, self.largestRectangleArea(row))
        return max_area
# @lc code=end

