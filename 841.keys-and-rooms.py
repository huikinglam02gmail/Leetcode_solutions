#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # Simple! BFS!
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        dq, visited = deque(), set()
        dq.append(0)
        visited.add(0)
        while dq:
            node = dq.popleft()
            for i in rooms[node]:
                if i not in visited:
                    dq.append(i)
                    visited.add(i)
        return len(visited) == n
# @lc code=end

