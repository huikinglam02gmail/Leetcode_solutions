#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#

# @lc code=start
from typing import List


class Solution:
    # First, define root to perform DFS. Let's choose that to be zero
    # We need to know the number of nodes in each subtree weight[i] to reach at the answer at O(n) time complexity
    # The answer array saves the total distance from the root
    # In the first DFS, we perform postorder traversal to calculate weight and answer
    # In the second DFS, we update the answer by this formula:
    # d[child] = d[parent] + n - weight[child] - weight[child]
    def dfs(self, node, parent, depth):
        count, distance = 1, depth
        for child in self.graph[node]:
            if child != parent:
                child_count, child_distance = self.dfs(child, node, depth + 1)
                count += child_count
                distance += child_distance
        self.weight[node] = count
        return [count, distance]
    
    def dfs2(self, node, parent, n):
        for child in self.graph[node]:
            if child != parent:
                self.answer[child] = self.answer[node] + n - 2*self.weight[child]
                self.dfs2(child, node, n)
        
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = [set() for i in range(n)]
        for edge in edges:
            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])
        self.weight = [0]*n
        self.answer = [0]*n
        root = 0
        [count, self.answer[root]] = self.dfs(root,-1,0)
        self.dfs2(root, -1, n)
        return self.answer
        
# @lc code=end

