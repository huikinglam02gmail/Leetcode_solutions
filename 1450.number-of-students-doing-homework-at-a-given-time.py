#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start
import heapq

class Solution:
    # Student starting later than queryTime will not affect the result
    # We can use min heap to keep track of start and end of all students
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        heap = []
        for start, end in zip(startTime, endTime):
            heapq.heappush(heap, [start, 1])
            heapq.heappush(heap, [end + 1, -1])
        active = 0
        while heap and heap[0][0] <= queryTime:
            time, status = heapq.heappop(heap)
            if status > 0:
                active += 1
            else:
                active -= 1
        return active
# @lc code=end

