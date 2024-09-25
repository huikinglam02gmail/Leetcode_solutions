#
# @lc app=leetcode id=2606 lang=python3
#
# [2606] Find the Substring With Maximum Cost
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    First assign the vals of each character
    Then store each previously seen prefix Sum in a min heap
    '''
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        Vals = [i + 1 for i in range(26)]
        for i in range(len(chars)): Vals[ord(chars[i]) - ord('a')] = vals[i]
        heap = []
        prefix = 0
        result = 0
        heapq.heappush(heap, 0)
        for c in s:
            prefix += Vals[ord(c) - ord('a')]
            result = max(result, prefix - heap[0])
            heapq.heappush(heap, prefix)
        return result
            
        
# @lc code=end

