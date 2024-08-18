#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
import heapq


class Solution:
    '''
    Use a heap to keep next smallest multiples of 2,3 and 5
    keep pushing in multiples of 2, 3 and 5 in the popped number    
    '''
    def nthUglyNumber(self, n: int) -> int: 
        heap, seen = [], set([1]) 
        heapq.heappush(heap, 1)
        for i in range(n):
            ugly = heapq.heappop(heap)
            for j in (2,3,5):
                if j * ugly not in seen:
                    heapq.heappush(heap, ugly * j)
                    seen.add(ugly * j)
        return ugly
# @lc code=end

