#
# @lc app=leetcode id=1722 lang=python3
#
# [1722] Minimize Hamming Distance After Swap Operations
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is a graph problem. The nodes are the indicies and the pairs in allowedSwaps link up the nodes 
    '''
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
# @lc code=end

