#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from typing import List


class Solution:
    # As the question is asking for all paths in a DAG, we can use DFS to achieve that goal
    # Regular DFS is applied
    def dfs(self, path, goal, curr):
        if curr == goal:
            self.result.append(path + [curr])
        else:
            for node in self.graph[curr]:
                self.dfs(path + [curr], goal, node)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        self.graph = graph
        self.result = []
        self.dfs([],n-1,0)
        return self.result
# @lc code=end

