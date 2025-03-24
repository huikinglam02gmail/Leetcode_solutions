#
# @lc app=leetcode id=3067 lang=python3
#
# [3067] Count Pairs of Connectable Servers in a Weighted Tree Network
#

# @lc code=start
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        self.graph = [{} for i in range(len(edges) + 1)]
        self.signalSpeed = signalSpeed
        for a, b, w in edges:
            self.graph[a][b] = w
            self.graph[b][a] = w
        
        result = [0] * (len(edges) + 1)
        for i in range(len(edges) + 1):
            pathSumDicts = []
            for nxt in self.graph[i]:
                pathSumDicts.append({})
                currentKey = self.graph[i][nxt] % signalSpeed
                pathSumDicts[-1][currentKey] = 1
                for k, v in self.dfs(nxt, i).items():
                    childrenKey = (self.graph[i][nxt] + k) % signalSpeed
                    pathSumDicts[-1][childrenKey] = pathSumDicts[-1].get(childrenKey, 0) + v
            connectables = []
            for pathSumDict in pathSumDicts:
                connectables.append(0)
                connectables[-1] += pathSumDict.get(0, 0)
            for j in range(len(connectables) - 1):
                for k in range(j + 1, len(connectables)): 
                    result[i] += connectables[j] * connectables[k]
        return result
             
    def dfs(self, node, prev):
        pathSumDict = {}
        for nxt in self.graph[node]:
            if nxt != prev:
                currentKey = self.graph[node][nxt] % self.signalSpeed
                pathSumDict[currentKey] = pathSumDict.get(currentKey, 0) + 1
                childrenDict = self.dfs(nxt, node)
                for child in childrenDict:
                    childrenKey = (self.graph[node][nxt] + child) % self.signalSpeed
                    pathSumDict[childrenKey] = pathSumDict.get(childrenKey, 0) + childrenDict[child]
        return pathSumDict    
# @lc code=end

