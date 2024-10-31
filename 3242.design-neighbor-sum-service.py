#
# @lc app=leetcode id=3242 lang=python3
#
# [3242] Design Neighbor Sum Service
#

# @lc code=start
from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.coord = [[-1, -1] for i in range(len(grid) * len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.coord[grid[i][j]][0] = i
                self.coord[grid[i][j]][1] = j

    def adjacentSum(self, value: int) -> int:
        result = 0
        if 0 <= self.coord[value][0] - 1 < len(self.grid) and 0 <= self.coord[value][1] < len(self.grid): result += self.grid[self.coord[value][0] - 1][self.coord[value][1]]
        if 0 <= self.coord[value][0] + 1 < len(self.grid) and 0 <= self.coord[value][1] < len(self.grid): result += self.grid[self.coord[value][0] + 1][self.coord[value][1]]
        if 0 <= self.coord[value][0] < len(self.grid) and 0 <= self.coord[value][1] - 1 < len(self.grid): result += self.grid[self.coord[value][0]][self.coord[value][1] - 1]
        if 0 <= self.coord[value][0] < len(self.grid) and 0 <= self.coord[value][1] + 1 < len(self.grid): result += self.grid[self.coord[value][0]][self.coord[value][1] + 1]
        return result

    def diagonalSum(self, value: int) -> int:
        result = 0
        if 0 <= self.coord[value][0] - 1 < len(self.grid) and 0 <= self.coord[value][1] - 1 < len(self.grid): result += self.grid[self.coord[value][0] - 1][self.coord[value][1] - 1]
        if 0 <= self.coord[value][0] - 1 < len(self.grid) and 0 <= self.coord[value][1] + 1 < len(self.grid): result += self.grid[self.coord[value][0] - 1][self.coord[value][1] + 1]
        if 0 <= self.coord[value][0] + 1 < len(self.grid) and 0 <= self.coord[value][1] - 1 < len(self.grid): result += self.grid[self.coord[value][0] + 1][self.coord[value][1] - 1]
        if 0 <= self.coord[value][0] + 1 < len(self.grid) and 0 <= self.coord[value][1] + 1 < len(self.grid): result += self.grid[self.coord[value][0] + 1][self.coord[value][1] + 1]
        return result


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
# @lc code=end

