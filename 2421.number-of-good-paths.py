#
# @lc app=leetcode id=2421 lang=python3
#
# [2421] Number of Good Paths
#

# @lc code=start
from typing import List

class UnionFindSet:
    def __init__(self, n=0):
        self.parents = [i for i in range(n)]
        self.count = n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            pMax, pMin = max(pu,pv), min(pu,pv)
            self.parents[pMax] = pMin
            self.count -= 1


# Union-find solution
class Solution:
    # Instead we can adopt a switch of thinking: if we try to build the graph with some preprocessing, we can avoid counting the non-good paths altogether
    # For example, if we sort the nodes according to vals, and then build the graph from small vals to large vals, good paths starting and ending with vals[i] and vals[i] will never pass through nodes with larger vals because those connections have not yet been added in
    # This then calls for the union-find algorithm to identify current clusters
    # We still considers edge formed between two nodes result in parent-child relationship between two nodes.
    # In another array we maintain node count of maximal value seen in all considered edges which is connected with the node.
    # Because we already sorted the edges, the new edges which contain the same vals will appear next to each other
    # When we add the second node with vals[i], the key question is: is the other node connected with the previous node with vals[i]?
    # We multiply the max count for the 2 parents
    # Then we conduct the union action
    # The maximum value count at the first parent would add that of second

    def maxValueCount(self, node, value):
        if value == self.max_values[node][0]:
            return self.max_values[node][1]
        else:
            return 0

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        UF = UnionFindSet(n)
        data = []
        for edge in edges:
            data.append([max(vals[edge[0]], vals[edge[1]])] + sorted(edge))
        data.sort()
        # max value node and number of paths that it is attached to
        self.max_values = [[vals[i], 1] for i in range(n)]
        result = n
        
        for val, node1, node2 in data:
            node1_p, node2_p = UF.find(node1), UF.find(node2)
            max_value_count_1, max_value_count_2 = self.maxValueCount(node1_p, val), self.maxValueCount(node2_p, val)
            result += max_value_count_1*max_value_count_2
            UF.union(node1_p, node2_p)
            self.max_values[node1_p] = [val, max_value_count_1 + max_value_count_2]
        return result
# @lc code=end

