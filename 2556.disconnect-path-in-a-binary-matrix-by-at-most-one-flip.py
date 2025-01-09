#
# @lc app=leetcode id=2556 lang=python3
#
# [2556] Disconnect Path in a Binary Matrix by at Most One Flip
#

# @lc code=start
from typing import List


class Solution:
    '''
    DFS from 0, 0 to m - 1, n - 1 once. Along the route mark all paths with 0
    Then DFS again from 0, 0 to m - 1, n - 1 again to see if it can reached by an alternative path without any overlap with all previously searched path
    '''
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        self.grid = grid
        if not self.dfs(0, 0): return True
        return not self.dfs(0, 0)
    
    def dfs(self, x, y):
        if x == len(self.grid) - 1 and y == len(self.grid[0]) - 1: return True
        if (x > 0 or y > 0): self.grid[x][y] = 0
        if 0 <= x + 1 < len(self.grid) and self.grid[x + 1][y] == 1 and self.dfs(x + 1, y): return True
        if 0 <= y + 1 < len(self.grid[0]) and self.grid[x][y + 1] == 1 and self.dfs(x, y + 1): return True     
        return False

        
# @lc code=end

