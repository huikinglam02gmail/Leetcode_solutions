#
# @lc app=leetcode id=3342 lang=python3
#
# [3342] Find Minimum Time to Reach Last Room II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        heap = []
        m, n = len(moveTime), len(moveTime[0])
        time = [[float("inf") for j in range(n)] for i in range(m)]
        heapq.heappush(heap, [0, 0, 0, 0])
        time[0][0] = 0
        while heap:
            t, x, y, moves = heapq.heappop(heap)
            if x == m - 1 and y == n - 1: return t
            if time[x][y] == t:
                neigs = [[x - 1, y], [x + 1, y], [x ,y - 1], [x, y + 1]]
                for x1, y1 in neigs:
                    if 0 <= x1 < m and 0 <= y1 < n:
                        t1 = max(moveTime[x1][y1], t)
                        t2 = t1 + 1 + moves % 2
                        if t2 < time[x1][y1]:
                            heapq.heappush(heap, [t2, x1, y1, moves + 1])
                            time[x1][y1] = t2
        return -1
                    
# @lc code=end

