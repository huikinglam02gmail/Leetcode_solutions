#
# @lc app=leetcode id=1938 lang=python3
#
# [1938] Maximum Genetic Difference Query
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each query, we are concerned about the DFS path from the root to a target node. And we are concerned about maximum XOR of a val to all nodes in the DFS path. Therefore, we can use a dynamic Trie concurrent with DFS to handle the problem. 
    But deleting a node from a Trie is troublesome. Instead we can use a array of prefix arrays to store all prefixes counts in the current path.
    First, build the graph.
    Then record the queries nodes, map to the indicies and the query value
    Next, we DFS from 0:
    1. Add the current node to the prefix tree.
    2. Ask if the current node is a key in the query dictionary.
    3. If so, find maximum XOR of the val with all values in the Trie, put the answer into result.
    4. If the current node has children in graph, DFS to each child node.
    5. When it's done, remove the current node from the Trie.
    '''
    def dfs(self, node):
        self.addNumToPrefixArray(node)
        for i, val in self.Q[node]:
            self.result[i] = self.getmaximumXOR(val)
        for child in self.graph[node]:
            self.dfs(child)
        self.removeNumFromPrefixArray(node)
    
    def addNumToPrefixArray(self, num):
        for i in range(self.totalLevels - 1, -1, -1):
            self.prefixTree[i][num >> i] += 1

    def removeNumFromPrefixArray(self, num):
        for i in range(self.totalLevels - 1, -1, -1):
            self.prefixTree[i][num >> i] -= 1

    def getmaximumXOR(self, val):
        result = 0
        for i in range(self.totalLevels - 1, -1, -1):
            valBit = (val >> i) & 1
            result <<= 1
            if self.prefixTree[i][result + (1 - valBit)] > 0:
                result += 1 - valBit
            else:
                result += valBit
        return result ^ val
    
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        self.graph = [set() for i in range(n)]
        self.Q = [[] for i in range(n)]
        self.result = [-1] * len(queries)
        self.totalLevels = (max(n - 1, max([val for node, val in queries]))).bit_length()
        self.prefixTree = [ [0 for j in range(1 << (self.totalLevels - i))] for i in range(self.totalLevels)]

        root = -1
        for i, c in enumerate(parents):
            if c != -1:
                self.graph[c].add(i)
            else:
                root = i
        
        for i, [node, val] in enumerate(queries):
            self.Q[node].append([i, val])
        
        self.dfs(root)
        return self.result

# @lc code=end

