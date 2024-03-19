#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    '''
    max heap to keep the count of tasks and when next task is available
    Use a queue to hold the popped out items
    At each time point, check the front of queue and append to the heap if time allows    
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        hash_table = {}
        for task in tasks:
            if task not in hash_table: hash_table[task] = 0
            hash_table[task] += 1
        for key in hash_table.keys(): heapq.heappush(heap, [- hash_table[key], 0])
        queue = deque()
        time = 0
        while queue or heap:
            while queue and queue[0][1] <= time:
                item = queue.popleft()
                heapq.heappush(heap, item)                
            if heap:
                item = heapq.heappop(heap)
                if item[0] < -1:
                    item[0] += 1
                    item[1] = time + n + 1
                    queue.append(item)
            time += 1
        return time
# @lc code=end

