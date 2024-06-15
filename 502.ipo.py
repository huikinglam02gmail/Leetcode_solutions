#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    First put the pairs together
    Sort according to capital
    if nothing in the heap, can stop here
    pop out the one with max profit
    '''
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        couples = []
        for i in range(len(capital)): couples.append((capital[i], profits[i]))
        couples.sort()
        heap = []
        i = 0
        while k > 0:
            while i < len(couples) and couples[i][0] <= w:
                heapq.heappush(heap, - couples[i][1])
                i += 1
            if not heap: return w
            w -= heapq.heappop(heap)
            k -= 1
        return w
                
                
# @lc code=end

