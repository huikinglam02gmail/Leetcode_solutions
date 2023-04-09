#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Firstly, topologically sort the graph: record adjacency of each node. 
    Start BFS from nodes at the top of topological order, only put in the nodes with adjacency = 0
    Record the color value of valid paths arriving at a node i: since colors space is limited, just record all the 26 colors
    If at the end of BFS we still see adjacency contains nonzero element, i.e. some nodes are not processed, we know we have cycles
    '''    

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [set() for i in range(n)]
        adjacency = [0] * n
        result = -1
        colorValues = [[0 for j in range(26)] for i in range(n)]

        for f, t in edges:
            graph[f].add(t)
            adjacency[t] += 1

        dq = deque()
        for i in range(n):
            if adjacency[i] == 0:
                dq.append(i)
        
        while dq:
            node = dq.popleft()
            colorValues[node][ord(colors[node]) - ord('a')] += 1
            result = max(result, colorValues[node][ord(colors[node]) - ord('a')])
            for nxt in graph[node]:
                for j in range(26):
                    colorValues[nxt][j] = max(colorValues[nxt][j], colorValues[node][j])
                adjacency[nxt] -= 1
                if adjacency[nxt] == 0:
                    dq.append(nxt)
        
        if sum(adjacency) > 0:
            return -1
        else:
            return result
 
# @lc code=end

