#
# @lc app=leetcode id=2976 lang=python3
#
# [2976] Minimum Cost to Convert String I
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    graph is supposed to be [{} for i in range(n)], with graph[i][j] = weight[i][j]
    return the SSP weight for all nodes
    O(n^2 log(n)) time
    '''
    def Dijkstra(self, graph, source):
        n = len(graph)
        result = [-1] * n
        heap = []
        visited = [False]*n
        visitedCount = 0
        heapq.heappush(heap, [0, source])

        while heap and visitedCount < n:
            weight, node = heapq.heappop(heap)
            if result[node] < 0:
                result[node] = weight
                visited[node] = True
                visitedCount += 1
                for nxt in graph[node].keys():
                    heapq.heappush(heap, [weight + graph[node][nxt], nxt])        
        return result
    
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [{} for i in range(26)]
        n = len(original)
        for i in range(n):
            if ord(changed[i]) - ord('a') not in graph[ord(original[i]) - ord('a')]: graph[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = float("inf")
            graph[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = min(graph[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')], cost[i])
        
        referenceTable = []
        for i in range(26): referenceTable.append(self.Dijkstra(graph, i))
        
        result = 0
        n = len(source)
        for i in range(n):
            if referenceTable[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == -1: return -1
            else: result += referenceTable[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
        return result
# @lc code=end

