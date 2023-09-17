#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    This is the traveling salesman problem
    Original DFS or BFS algorithms cannot be used directly because the search will involve revisiting nodes
    given n <= 12, it hints we can use bitmask to represent states
    We can still conduct BFS, but we need to include what we visited before in addition to current node id as the state.
    Practically we brute force search for all the shortest paths starting from all the nodes.
    Each step we include all possible neighbours and push into the queue
    How to avoid infinite cycles? For example in Example 1: graph = [[1,2,3],[0],[0],[0]]
    To avoid cycling between 0 and 2, when we start searching from 2, first we add (2, 0100)
    Then we are at (0,0101), then (2,0101). We cannot proceed forward because (0,0101) is already visited, steps = 2 
    '''
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        dq, visited = deque(), set()
        n, steps = len(graph), 0
        for i in range(n):
            dq.append([i, 1 << i])
            visited.add((i, 1 << i))
        while dq:
            for i in range(len(dq)):
                node, mask = dq.popleft()
                if mask == (1 << n) - 1:
                    return steps
                for nxt in graph[node]:
                    new_mask = mask | (1 << nxt)
                    if (nxt, new_mask) not in visited:
                        dq.append([nxt, new_mask])
                        visited.add((nxt, new_mask))
            steps += 1
# @lc code=end

