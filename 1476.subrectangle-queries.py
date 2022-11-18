#
# @lc app=leetcode id=1476 lang=python3
#
# [1476] Subrectangle Queries
#

# @lc code=start
from typing import List


class SubrectangleQueries:
    # Prefix sum won't work
    # Brute force updating should be doable, but it's too slow
    # Instead we can track what was modified before
    # Just search if the coordinate of interest is ever modified
    def __init__(self, rectangle: List[List[int]]):
        self.modified = []
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.modified.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        n = len(self.modified)
        for i in range(n-1, -1, -1):
            row1, col1, row2, col2, value = self.modified[i]
            if row1 <= row <= row2 and col1 <= col <= col2:
                return value
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
# @lc code=end

