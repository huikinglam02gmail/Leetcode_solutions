#
# @lc app=leetcode id=1627 lang=python3
#
# [1627] Graph Connectivity With Threshold
#

# @lc code=start
from typing import List


class Solution:
    # Build the graph from i = threshold + 1 by multiplying 2*i, 3*i,..., until it reaches n
    # We only need to consider the primes.
    # We then build the disjoint set and handle the queries
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        
# @lc code=end

