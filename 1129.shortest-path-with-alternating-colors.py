#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # Shortest path: BFS
    # Because we are only looking for paths with alternating color
    # We define two nodes (i, 0 or 1)
    # 0 = it is from a red edge; 1 = it is from a blue edge
    
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Build the graph
        graph = {(0,0): set(), (0,1): set()}
        for src, dest in redEdges:
            if (src,1) not in graph:
                graph[(src,1)] = set()
            graph[(src,1)].add((dest, 0))
        for src, dest in blueEdges:
            if (src,0) not in graph:
                graph[(src,0)] = set()
            graph[(src,0)].add((dest, 1))
        
        # BFS
        result = [float('inf')]*n
        dq, visited, steps = deque(), set(), 0
        dq.append((0,0))
        dq.append((0,1))
        while dq:
            for i in range(len(dq)):
                node, color = dq.popleft()
                result[node] = min(result[node], steps)
                if (node,color) in graph:
                    for nxt in graph[(node,color)]:
                        if nxt not in visited:
                            dq.append(nxt)
                            visited.add(nxt)
            steps += 1
        for i in range(n):
            if result[i] == float('inf'):
                result[i] = -1
        return result
# @lc code=end

