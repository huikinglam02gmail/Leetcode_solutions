#
# @lc app=leetcode id=1568 lang=python3
#
# [1568] Minimum Number of Days to Disconnect Island
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # This problem is related to the number of island problem
    # We should first find the number of islands in the grid
    # If there is more than 1, just return 0
    # If there is 1, we then try to change one of the grid members to 0 and run number of island code again
    # If any of them result in more than 1 island, we return 1
    # Otherwise, return 2
    # Reason: we can always use the deletions to given an isolated island on the edge, as shown in Example 1
    
    def numIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dq = deque()
                    dq.append((i,j))
                    visited.add((i,j))
                    while dq:
                        node = dq.popleft()
                        neigs = [[0,1],[1,0],[-1,0],[0,-1]]
                        for neig in neigs:
                            new_node = (node[0] + neig[0], node[1] + neig[1])
                            if m > new_node[0] >= 0 <= new_node[1] < n and new_node not in visited and grid[new_node[0]][new_node[1]] == 1:
                                dq.append(new_node)
                                visited.add(new_node)
                    result += 1
        return result

    def minDays(self, grid: List[List[int]]) -> int:
        initialIslands = self.numIslands(grid)
        if initialIslands != 1:
            return 0
        else:
            m, n = len(grid), len(grid[0])
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                        modifiedIslands = self.numIslands(grid)
                        if modifiedIslands != 1:
                            return 1
                        grid[i][j] = 1
            return 2
        
# @lc code=end

