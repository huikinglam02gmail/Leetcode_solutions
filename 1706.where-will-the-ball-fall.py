#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#

# @lc code=start
class Solution:
    # DFS row by row down
    def dfs(self, j, i):
        if i == self.m:
            return j
        if self.grid[i][j] == 1:
            if j < self.n-1 and self.grid[i][j+1] == 1:
                return self.dfs(j+1, i+1)
        else:
            if j > 0 and self.grid[i][j-1] == -1:
                return self.dfs(j-1, i+1)
        return -1

    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        result = []
        for j in range(self.n):
            result.append(self.dfs(j, 0))
        return result
# @lc code=end

