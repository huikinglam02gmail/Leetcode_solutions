#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        seenNodes = set()
        result = 0
        for i in range(n):
            if i not in seenNodes:
                local = set()
                dq = deque()
                dq.append(i)
                local.add(i)
                while dq:
                    node = dq.popleft()
                    for nxt in graph[node]:
                        if nxt not in local:
                            local.add(nxt)
                            dq.append(nxt)
                localList = list(local)
                if len(localList) == 1:
                    result += 1
                else:
                    edgeFound = True
                    for j in range(len(localList) - 1):
                        for k in range(j + 1, len(localList)):
                            edgeFound &= (localList[j] in graph[localList[k]])
                    if edgeFound: result += 1
                seenNodes = seenNodes | local
        return result
# @lc code=end

