#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#

# @lc code=start
from typing import List


class Solution:
    # 1 <= m*n <= 20
    # Can use bitmask to represent whether a point is visited
    # The approach is practically brute force. We can first map all free coordinates (including the start and end) to numbers.
    # Then we can dfs from the source to end using bitmask to represent visited points
    
    def dfs(self, row, col, state):
        #print(row, col, state)
        if row == self.end[0] and col == self.end[1]:
            if state == pow(2,self.count)-1:
                self.result += 1
        else:
            neighbours = [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]
            for neighbour in neighbours:
                if neighbour in self.mapping:
                    i = self.mapping[neighbour]
                    if state & (1 << i) == 0:
                        self.dfs(neighbour[0], neighbour[1], state ^ (1 << i))
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.count, self.mapping, self.result = 0, {}, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    self.mapping[(i,j)] = self.count
                    self.count += 1
                if grid[i][j] == 1:
                    self.start = [i,j]
                    state = 1 << (self.count-1)
                if grid[i][j] == 2:
                    self.end = [i,j]
        self.dfs(self.start[0], self.start[1], state)
        return self.result
# @lc code=end

