#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hash_table = {}
        for edge in edges:
            for node in edge:
                if node in hash_table:
                    hash_table[node] += 1
                    return node
                else:
                    hash_table[node] = 1
# @lc code=end

