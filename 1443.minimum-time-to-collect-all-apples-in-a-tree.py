#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start
class Solution:
    # For each edge, it is traversed twice if it leads to any apple
    # So, DFS from 0
    # For each node, we record its parent node, and the edge which leads to it 
    # Then we then DFS all its children nodes
    # The result to return is number of edge traversals to fully explore the current subtree
    # we add 2 to it if the node has apple
    
    def dfs(self, node, parent):
        result = 0
        for nxt in self.graph[node]:
            if nxt != parent:
                result += self.dfs(nxt, node)
        if self.hasApple[node] or result > 0:
            result += 2
        return result
        
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.graph = [set() for i in range(n)]
        self.hasApple = hasApple
        for start, end in edges:
            self.graph[start].add(end)
            self.graph[end].add(start)
        result = self.dfs(0, -1)
        if result > 0:
            result -= 2
        return result
# @lc code=end

