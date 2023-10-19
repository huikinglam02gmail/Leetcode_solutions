#
# @lc app=leetcode id=1948 lang=python3
#
# [1948] Delete Duplicate Folders in System
#

# @lc code=start
from typing import List


class Solution:
    '''
    This question is about serializing a node's children, and removing nodes with identical children
    Looking at the example, we notice the answer always is a subset of paths. So we need to decide which to delete.
    To serialize a subtree, we use the JSON convention: for example, subtree of the root in examples can be represented by
    1: [{a:b},{c:b},{d:a}]
    2: [{a:{b:{x:y}}},{c:b},{w:y}]
    3: [{a:b},{c:d}]
    We can sort paths by length first
    Then for each increment length, recognize the parent of each node, build the graph
    Then dfs from the top: for eacb children, serialize the subtree.
    Save the serialization as key in dict and delete node with keys that appear more than once.
    '''
    
    def dfs(self, node):
        n = len(self.graph[node])
        nodesSorted = sorted(self.graph[node], key = lambda x: self.paths[x][-1])
        result = ""
        if n > 0: result += ":"
        if n > 1: result += "["
        for i in range(n):
            result += "{"
            result += self.dfs(nodesSorted[i])
            result += "}"
            if i < n - 1: result += ","
        if n > 1: result += "]"

        if result: 
            if result not in self.subtreeIndexMap:
                self.subtreeIndexMap[result] = set()            
            self.subtreeIndexMap[result].add(node)
        return self.paths[node][-1] + result

    def dfsThrow(self, node):
        self.KeysToThrow.add(node)
        for child in self.graph[node]:
            if child not in self.KeysToThrow:
                self.dfsThrow(child)

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        data = [[len(path), i] for i, path in enumerate(paths)]
        data.sort()
        self.paths = paths
        n = len(data)
        self.graph = [[] for i in range(n)]
        j = 0
        cur = 0
        prev = set()
        serializedPathToIndex = {}
        self.subtreeIndexMap = {}
        dfsStartNodes = set()
        while j < n:
            cur += 1
            next = set()
            while j < n and data[j][0] == cur:
                pathSerialized = ",".join(paths[data[j][1]])
                parentSerialized = ",".join(paths[data[j][1]][:-1])
                if parentSerialized in prev:
                    self.graph[serializedPathToIndex[parentSerialized]].append(data[j][1])
                serializedPathToIndex[pathSerialized] = data[j][1]
                next.add(pathSerialized)
                j += 1
            if cur == 1:
                dfsStartNodes = set([serializedPathToIndex[i] for i in next])
            prev = next
        
        for node in dfsStartNodes:
            self.dfs(node)

        self.KeysToThrow = set()
        for indices in self.subtreeIndexMap.values():
            if len(indices) > 1:
                for i in indices:
                    if i not in self.KeysToThrow:
                        self.dfsThrow(i)
        result = []
        for i in range(n):
            if i not in self.KeysToThrow:
                result.append(paths[i])
        return result
# @lc code=end

