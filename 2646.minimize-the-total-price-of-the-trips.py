#
# @lc app=leetcode id=2646 lang=python3
#
# [2646] Minimize the Total Price of the Trips
#

# @lc code=start
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    '''
    Each trip only has one possible path. Therefore we know what is the final price if not including the nonadjacent nodes flip. It is the sum of price of each node times frequency of visit to each node.
    To include the nonadjacent node flip condition, we can se dynamic programming to compare the 2 scenarios: a certain node is either flip or not flipped. Keep both results: if we flip the current node, the neighbour nodes must not be flipped; Otherwise, the neighbour nodes can be both flip or not flipped, just take the minimum. DFS will achieve the purpose
    '''
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph =  [set() for i in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        frequency = [0]*n
        for start, end in trips:
            dq = deque()
            visited = set()
            dq.append([start])
            visited.add(start)
            while dq:
                visitedNodes = dq.popleft()
                if visitedNodes[-1] == end:
                    for visitedNode in visitedNodes:
                        frequency[visitedNode] += 1
                    break
                for nxt in graph[visitedNodes[-1]]:
                    if nxt not in visited:
                        dq.append(visitedNodes + [nxt])
                        visited.add(nxt)

        @lru_cache(None)
        def dfs(node, parent, halfThisNode):
            result = price[node] * frequency[node]
            if halfThisNode:
                result //= 2
            for nxt in graph[node]:
                if nxt != parent:
                    nxtNodeNotFlip = dfs(nxt, node, False)
                    nxtNodeFlip = dfs(nxt, node, True)
                    if halfThisNode:
                        result += nxtNodeNotFlip
                    else:
                        result += min(nxtNodeFlip, nxtNodeNotFlip)
            return result

        return min(dfs(0, -1, True), dfs(0, -1, False))


# @lc code=end

