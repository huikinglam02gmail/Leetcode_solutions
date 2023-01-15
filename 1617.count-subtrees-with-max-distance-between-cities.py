#
# @lc app=leetcode id=1617 lang=python3
#
# [1617] Count Subtrees With Max Distance Between Cities
#

# @lc code=start
from typing import List


class Solution:
    # 2 <= n <= 15
    # possible to use bitmask to represent every state
    # So given a state, we can dfs from any node 
    # and ask if we can reach every node inside the set
    # If so, it is a valid subset
    # For the DFS, we make use of the diameter of tree algorithm:
    # Longest path between any two nodes within a substree is equal to maximum of:
    # 1. Longest path within the subtree formed by any of its children node
    # 2. Sum of 2 maximum heights that can be reached from the node
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        
# @lc code=end

