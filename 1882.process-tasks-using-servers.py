#
# @lc app=leetcode id=1882 lang=python3
#
# [1882] Process Tasks Using Servers
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    '''
    Simulate the process
    '''
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = []
        busy = []
        for i, s in enumerate(servers):
            heapq.heappush(free, [s, i, 0])
        ans = []
        for j, task in enumerate(tasks):
            while not free or (busy and busy[0][0] <= j):
                endTime, w, i = heapq.heappop(busy)
                heapq.heappush(free, [w, i, endTime])
            w, i, time = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, [max(time, j) + task, w, i])
        return ans

        
# @lc code=end
