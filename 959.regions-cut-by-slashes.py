#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Scale up the grid
    Or rather, for a grid point at (i,j), we define instead four grid points within the grid [4*i+1, 4*j+2], [4*i+2, 4*j+3], [4*i+3, 4*j+2], [4*i+2, 4*j+1] (N,E,S,W)
    If the string is " ", we connect them all next to each other
    If the string is "/", we connect them N, W and S, E
    If the string is "\", we connect them N, E and S, W
    Also, N is connected with S of last row, i.e. [4*i+1, 4*j+2] to connect with [4*i-1, 4*j+2] i.e. candidate - 2    
    '''   
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, nodes = len(grid), []
        graph = {}
        for i in range(n):
            for j in range(n):
                candidates = [(4 * i + 1, 4 * j + 2), (4 * i + 2, 4 * j + 3), (4 * i + 3, 4 * j + 2), (4 * i + 2, 4 * j + 1)]
                for candidate in candidates:
                    graph[candidate] = set()
                    nodes.append(candidate)

        # Build the graph
        for i in range(n):
            for j in range(n):
                candidates = [(4 * i + 1, 4 * j + 2), (4 * i + 2, 4 * j + 3), (4 * i + 3, 4 * j + 2), (4 * i + 2, 4 * j + 1)]
                for k, candidate in enumerate(candidates):
                    if k == 0 and (candidate[0] - 2, candidate[1]) in graph:
                        graph[candidate].add((candidate[0] - 2, candidate[1]))
                        graph[(candidate[0] - 2, candidate[1])].add(tuple(candidate))
                    elif k == 1 and (candidate[0], candidate[1] + 2) in graph:
                        graph[candidate].add((candidate[0], candidate[1] + 2))
                        graph[(candidate[0], candidate[1] + 2)].add(candidate)
                    elif k == 2 and (candidate[0] + 2, candidate[1]) in graph:
                        graph[candidate].add((candidate[0] + 2, candidate[1]))
                        graph[(candidate[0] + 2, candidate[1])].add(candidate)
                    elif k == 3 and (candidate[0], candidate[1] - 2) in graph:
                        graph[candidate].add((candidate[0], candidate[1] - 2))
                        graph[(candidate[0], candidate[1] - 2)].add(candidate)
                if grid[i][j] == " ":
                    connections = [[0, 1, 2, 3]]
                elif grid[i][j] == "/":
                    connections = [[0, 3], [1, 2]]
                else:
                    connections = [[0, 1], [2, 3]]
                for connection in connections:
                    for k in range(len(connection) - 1):
                        graph[candidates[connection[k]]].add(candidates[connection[k + 1]])
                        graph[candidates[connection[k + 1]]].add(candidates[connection[k]])
        
        # BFS... finally
        visited, regions = set(), 0
        for node in nodes:
            if node not in visited:
                regions += 1
                dq = deque()
                dq.append(node)
                visited.add(node)
                while dq:
                    i = dq.popleft()
                    for nxt in graph[i]:
                        if nxt not in visited:
                            dq.append(nxt)
                            visited.add(nxt)
        return regions
# @lc code=end

