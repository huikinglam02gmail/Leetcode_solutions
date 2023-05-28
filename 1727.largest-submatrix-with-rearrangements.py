#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is essentially Leetcode 85 Maximal Rectangle. Each time we find the maximum rectangle in histogram for each row, we know we will get the largest rectangle if we can sort the counts 
    '''
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
    
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(matrix)):
            if i == 0:
                row = matrix[i].copy()
            else:
                for j in range(len(row)):
                    if matrix[i][j] == 0:
                        row[j] = 0
                    else:
                        row[j] += matrix[i][j]
            max_area = max(max_area, self.largestRectangleArea(sorted(row)))
        return max_area
# @lc code=end

