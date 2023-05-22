#
# @lc app=leetcode id=1722 lang=python3
#
# [1722] Minimize Hamming Distance After Swap Operations
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    This is a graph problem. The nodes are the indicies and the pairs in allowedSwaps link up the nodes
    Then each connected component, we count occurrence of each number for both source and target. Whenever occurrence of a number in target > source, we increment the result by the difference
    '''
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = [set() for i in range(len(source))]
        for a, b in allowedSwaps:
            graph[a].add(b)
            graph[b].add(a)
        
        visited = set()
        result = 0
        for i in range(len(source)):
            if i not in visited:
                dq = deque()
                local = set()
                dq.append(i)
                local.add(i)
                while dq:
                    node = dq.popleft()
                    for nxt in graph[node]:
                        if nxt not in local:
                            dq.append(nxt)
                            local.add(nxt)
                sourceDict = {}
                targetDict = {}
                for j in local:
                    if target[j] not in targetDict:
                        targetDict[target[j]] = 0
                    if source[j] not in sourceDict:
                        sourceDict[source[j]] = 0
                    sourceDict[source[j]] += 1
                    targetDict[target[j]] += 1
                for key in targetDict.keys():
                    result += max(0, targetDict[key] - sourceDict.get(key, 0))
                visited |= local
        return result                   
# @lc code=end

