#
# @lc app=leetcode id=2360 lang=python3
#
# [2360] Longest Cycle in a Graph
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Each node has at most one outgoing edge. Therefore, any cycle can be constructed by DFSing from root nodes. Also mark node as visited.
    To ensure the DFS starts with the nodes higher in the topological order, we first record the adjacencies of different nodes, and start with nodes that have no incoming edges. During the DFS, we record for each arrived node, the number of steps from the DFS root. 
    '''

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        adjacencies = [0]*n
        visited = [False]*n
        for i, edge in enumerate(edges):
            adjacencies[edge] += 1
        
        dq = deque()
        result = -1
        adjacencies = [[v, i] for i, v in enumerate(adjacencies)]
        adjacencies.sort()
        for i in range(n):
            appeared = {}
            dq.append([adjacencies[i][1], 0])
            visited[adjacencies[i][1]] = True
            appeared[adjacencies[i][1]] = 0
            while dq:
                node, cycleLength = dq.popleft()
                if edges[node] != -1:
                    nxt = edges[node]
                    if visited[nxt] == False:
                        visited[nxt] = True
                        appeared[nxt] = cycleLength + 1
                        dq.append([nxt, cycleLength + 1])
                    elif nxt in appeared:
                        result = max(result, cycleLength + 1 - appeared[nxt])
        return result


# @lc code=end

