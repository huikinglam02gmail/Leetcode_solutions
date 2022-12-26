#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dq = deque()
                    dq.append((i,j))
                    grid[i][j] = "0"
                    while dq:
                        node = dq.popleft()
                        neigs = [[0,1],[1,0],[-1,0],[0,-1]]
                        for neig in neigs:
                            new_node = (node[0] + neig[0], node[1] + neig[1])
                            if m > new_node[0] >= 0 <= new_node[1] < n and grid[new_node[0]][new_node[1]] == "1":
                                dq.append(new_node)
                                grid[new_node[0]][new_node[1]] = "0"
                    result += 1
        return result
# @lc code=end

