#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        chain = []
        for pair in pairs:
            if not chain or pair[0] > chain[-1]:
                chain.append(pair[1])
        return len(chain)
# @lc code=end

