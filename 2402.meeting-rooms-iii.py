#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [i for i in range(n)]
        room_count = [0] * n
        close_time = []
        for start, end in meetings:
            while close_time and start >= close_time[0][0]:
                heapq.heappush(rooms, heapq.heappop(close_time)[1])
            delay = 0
            if rooms:
                room = heapq.heappop(rooms)
            else:
                endtime, room =  heapq.heappop(close_time)
                delay += endtime - start
            room_count[room] += 1
            heapq.heappush(close_time, [end + delay, room])
        maxCount = max(room_count)
        for i in range(n):
            if room_count[i] == maxCount: return i
        return -1
# @lc code=end

