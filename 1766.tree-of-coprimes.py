#
# @lc app=leetcode id=1766 lang=python3
#
# [1766] Tree of Coprimes
#

# @lc code=start
from typing import List
import math


class Solution:
    '''
    1 <= nums[i] <= 50
    So we can first find all the possible coprime pairs from 1 to 50.
    Then build the graph
    From root, we DFS out and keep a dictionary of how many steps each node on path is away from the root. 
    i.e. dict[nums[i]] = [node index, steps]
    we only care about the last appearance of coprimes, and we scan all the possible coprimes and find the minimum index.
    '''
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        coPrimes = [set() for i in range(51)]
        for i in range(1, 51, 1):
            for j in range(i, 51, 1):
                if math.gcd(i, j) == 1:
                    coPrimes[i].add(j)
                    coPrimes[j].add(i)

        graph = [set() for i in range(len(nums))]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        result = [-1]*len(nums)
        numseen = {}
        onpath = set()

        def dfs(node, steps):
            lastIndex = -1
            minDist = float('inf')
            for cop in coPrimes[nums[node]]:
                if cop in numseen and len(numseen[cop]) > 0 and (steps - numseen[cop][-1][-1]) < minDist:
                    minDist = steps - numseen[cop][-1][-1]
                    lastIndex = numseen[cop][-1][0]
            result[node] = lastIndex
            onpath.add(node)
            if (nums[node] not in numseen):
                numseen[nums[node]] = []
            numseen[nums[node]].append([node, steps])
            for nxt in graph[node]:
                if nxt not in onpath:
                    dfs(nxt, steps + 1)
            onpath.remove(node)
            numseen[nums[node]].pop()
        
        dfs(0, 0)
        return result
                

# @lc code=end
