#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution:
    '''
    DFS solution
    Safe nodes = nodes not in cycle
    Strategy: DFS from each node and record the path nodes when a cycle is detected
    For a node to be safe, all the path went out from it do not encounter a cycle
    When conducting DFS, we do not need to search nodes previously proven to be safe
    Also we do not search the known cycle nodes    
    '''
    def dfs(self, node, path):
        if node in set(path):
            for item in path:
                self.cycle_nodes.add(item)
            return False
        else:
            for nxt in self.graph[node]:
                if nxt not in self.safe_nodes and not self.dfs(nxt, path + [node]):
                    return False
            self.safe_nodes.add(node)
            return True    

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.graph = graph
        self.safe_nodes = set()
        self.cycle_nodes = set()
        for i in range(len(graph)):
            if i not in self.cycle_nodes:
                self.dfs(i, [])
        return sorted(list(self.safe_nodes))
# @lc code=end

