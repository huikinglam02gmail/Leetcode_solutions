#
# @lc app=leetcode id=2127 lang=python3
#
# [2127] Maximum Employees to Be Invited to a Meeting
#

# @lc code=start
from typing import List


class Solution:
    '''
    There are two possibilities:
    1. The max seating arrangement are employees forming a large cycle. In cycle size > 2, only nodes on the cycle can be in the arrangement.
    2. All for cycle with size 2, the cycle with the longest acyclical path the cycle can be accomodated
    '''
    def sizeTwoDfs(self, node, prev):
        result = 1
        self.visited[node] = True
        for nxt in self.graph[node]:
            if nxt != prev: result = max(result, 1 + self.sizeTwoDfs(nxt, node))
        return result

    def otherSizeDfs(self, node, prev):
        self.visited[node] = True
        result = - float("inf")
        for nxt in self.graph[node]:
            if not self.visited[nxt]:
                self.nodesOnPath.add(nxt)
                result = max(result, self.otherSizeDfs(nxt, node))
            elif nxt in self.nodesOnPath:
                result = max(result, len(self.nodesOnPath))
            if nxt in self.nodesOnPath: self.nodesOnPath.remove(nxt)
        return result

    def maximumInvitations(self, favorite: List[int]) -> int:
        self.graph = [set() for i in range(len(favorite))]
        self.size2Cycle = set()
        for i, fav in enumerate(favorite): 
            self.graph[fav].add(i)
            if favorite[fav] == i: 
                self.size2Cycle.add(i)

        self.visited = [False for i in range(len(favorite))]
        result = 0
        for size2node in self.size2Cycle:
            if not self.visited[size2node]: result += self.sizeTwoDfs(size2node, favorite[size2node])
            if not self.visited[favorite[size2node]]: result += self.sizeTwoDfs(favorite[size2node], size2node)
        for i in range(len(favorite)):
            if not self.visited[i]:
                self.nodesOnPath = set()
                self.nodesOnPath.add(i)
                result = max(result, self.otherSizeDfs(i, -1))
        return result
# @lc code=end

