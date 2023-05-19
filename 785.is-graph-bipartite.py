#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''    
    Since bipartite means every edge connects between 2 different set, our goal is to find out which set a point belongs to
    Therefore, starting from 0, we carry out BFS to search itself and its neighbours and partition them into the sets. If we find an edge which connects a node to node in the same set, we return False 
    '''

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        inSet = [-1] * n
        for i in range(n):
            if inSet[i] == -1:
                dq = deque()
                dq.append(i)                
                inSet[i] = 0
                while dq:
                    node = dq.popleft()
                    for j in graph[node]:
                        if inSet[j] == inSet[node]:
                            return False
                        elif inSet[j] == - 1:
                            inSet[j] = 1 - inSet[node]
                            dq.append(j)
        return True
# @lc code=end

