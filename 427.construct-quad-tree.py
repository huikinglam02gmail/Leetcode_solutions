#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List


class Solution:
    def helper(self, x, y, n):
        if n == 1:
            return Node(self.grid[x][y], True, None, None, None, None)
        else:
            quad = []
            # divide into 4 parts
            for i in range(4):
                if i == 0:
                    quad.append(self.helper(x, y, n // 2))
                if i == 1:
                    quad.append(self.helper(x, y + n // 2, n // 2))
                if i == 2:
                    quad.append(self.helper(x + n // 2, y, n // 2))
                if i == 3:
                    quad.append(self.helper(x + n // 2, y + n // 2, n // 2))
            all_leaves = True
            all_match = True
            value = self.grid[x][y]
            for item in quad:
                all_leaves &= item.isLeaf
                all_match &= item.val == value
            if all_leaves and all_match:
                return Node(self.grid[x][y], True, None, None, None, None)
            else:
                return Node(1, False, quad[0], quad[1], quad[2], quad[3])    
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid      
        return self.helper(0,0,len(grid))
                
        
# @lc code=end

