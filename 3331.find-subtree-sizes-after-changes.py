#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from typing import List


class Solution:
    '''
    1. from parent, generate the children map
    2. DFS from root and along the DFS path, keep track of last parent by stack for each character. Rewire parent
    3. DFS again from parent, now reporting subtree size
    '''
    def generateChildrenFromParent(self):
        n = len(self.parent)
        children = [set() for i in range(n)]
        for i in range(n): 
            if self.parent[i] >= 0: children[self.parent[i]].add(i)
        return children
    
    def dfs1(self, node):
        if self.ancestors[ord(self.s[node]) - ord('a')]: self.parent[node] = self.ancestors[ord(self.s[node]) - ord('a')][-1]
        self.ancestors[ord(self.s[node]) - ord('a')].append(node)
        for nxt in self.children[node]: self.dfs1(nxt)
        self.ancestors[ord(self.s[node]) - ord('a')].pop()
    
    def dfs2(self, node):
        subTreeSize = 1
        for nxt in self.children[node]: subTreeSize += self.dfs2(nxt)
        self.result[node] += subTreeSize
        return subTreeSize


    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        self.parent = parent
        self.children = self.generateChildrenFromParent()
        self.s = s
        self.ancestors = [[] for i in range(26)]
        self.dfs1(0)
        self.children = self.generateChildrenFromParent()
        self.result = [0] * len(self.parent)
        totalNodeCount = self.dfs2(0)
        return self.result

        
# @lc code=end

