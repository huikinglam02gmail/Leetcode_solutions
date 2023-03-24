#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    The goal is to flip all outgoing path from 0. Therefore, we can BFS from 0, starting with an undirected graph. When we build the graph, we also record the edge id. So later when we BFS, we also ask if the edge we use is forward going or reversed. If it is forward going, we add 1 to the result    
    '''

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        for i, connection in enumerate(connections):
            u, v = connection
            graph[u].add((v, i))
            graph[v].add((u, i))
        
        dq, result = deque(), 0
        visited = [False for i in range(n)]
        dq.append(0)
        visited[0] = True
        while dq:
            node = dq.popleft()
            for nxt, ind in graph[node]:
                if not visited[nxt]:
                    if connections[ind] == [node, nxt]:
                        result += 1
                    dq.append(nxt)
                    visited[nxt] = True
        return result
# @lc code=end

