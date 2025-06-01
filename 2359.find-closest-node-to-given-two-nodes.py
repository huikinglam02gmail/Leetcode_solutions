#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS fromn node1 to all other nodes, record the distance
    Do the same for node2
    Then find the index    
    '''
    def bfs(self, startNode, distanceArray):
        dq = deque()
        visited = set()
        dq.append(startNode)
        visited.add(startNode)
        steps = 0
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                distanceArray[node] = min(distanceArray[node], steps)
                for nxt in self.graph[node]:
                    if nxt not in visited:
                        visited.add(nxt)
                        dq.append(nxt)
            steps += 1
        return distanceArray
    
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [n]*n
        dist2 = [n]*n
        self.graph = [set() for i in range(n)]
        for i, nxt in enumerate(edges):
            if nxt != -1:
                self.graph[i].add(nxt)

        dist1 = self.bfs(node1, dist1)
        dist2 = self.bfs(node2, dist2)
        
        minSoFar = n
        minIndex = -1
        for i in range(n):
            if max(dist1[i], dist2[i]) < minSoFar:
                minIndex = i
                minSoFar = max(dist1[i], dist2[i])
        return minIndex
        

# @lc code=end

