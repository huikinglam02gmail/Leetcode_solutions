#
# @lc app=leetcode id=2538 lang=python3
#
# [2538] Difference Between Maximum and Minimum Price Sum
#

# @lc code=start
from typing import List


class Solution:
    # We use rerooting to solve the problem.
    # Firstly, we DFS from a random node, (choose 0 for the problem)
    # In the process, we record the subtree sum excluding the current point
    # Next, we dfs a second time, this time we compare the maximum cost path from its children vs its parent
    # If the considered child is the one giving maximum path cost, we provide the max between the second largest sibling and parent for dfs downstream
    # Otherwise we provide the largest sibling and parent
    
    def dfs(self, node, parent):
        m = 0
        for nxt in self.graph[node]:
            if nxt == parent:
                continue
            else:
                m = max(m, self.dfs(nxt, node))
        self.subtreeSum[node] = m + self.price[node]
        return m + self.price[node]
    
    def dfs2(self, node, parent, parentContribution):
        maxChild = -1
        largestChildContribution = 0
        secondChildContribution = 0
        for nxt in self.graph[node]:
            if nxt == parent:
                continue
            elif self.subtreeSum[nxt] > largestChildContribution:
                secondChildContribution = largestChildContribution
                largestChildContribution = self.subtreeSum[nxt]
                maxChild = nxt
            elif self.subtreeSum[nxt] > secondChildContribution:
                secondChildContribution = self.subtreeSum[nxt]
        
        self.result = max(self.result, largestChildContribution, parentContribution)
        for nxt in self.graph[node]:
            if nxt == parent:
                continue
            elif nxt == maxChild:
                self.dfs2(nxt, node, self.price[node] + max(parentContribution, secondChildContribution))
            else:
                self.dfs2(nxt, node, self.price[node] + max(parentContribution, largestChildContribution))

    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        self.graph = [set() for i in range(n)]
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)

        self.subtreeSum = [0]*n
        self.price = price
        self.result = 0
        rootSubTreeSum = self.dfs(0, -1)
        self.dfs2(0,-1,0)
        return self.result
# @lc code=end

