#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    First mark the islands by island index 2 vs 3
    Then BFS from island 3 to island 2    
    '''

    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n, count = len(grid), len(grid[0]), 2
        neigs = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dq = deque()
                    dq.append((i,j))
                    grid[i][j] = count
                    while dq:
                        node = dq.popleft()
                        for neig in neigs:
                            nxt = (node[0] + neig[0], node[1] + neig[1])
                            if 0 <= nxt[0] < m and 0 <= nxt[1] < n and grid[nxt[0]][nxt[1]] == 1:
                                dq.append(nxt)
                                grid[nxt[0]][nxt[1]] = count
                    count += 1
        
        dq, steps = deque(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 3:
                    dq.append((i, j))            
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                for neig in neigs:
                    nxt = (node[0] + neig[0], node[1] + neig[1])
                    if 0 <= nxt[0] < m and 0 <= nxt[1] < n and grid[nxt[0]][nxt[1]] != 3:
                        if grid[nxt[0]][nxt[1]] == 2:
                            return steps
                        dq.append(nxt)
                        grid[nxt[0]][nxt[1]] = 3
            steps += 1
# @lc code=end

