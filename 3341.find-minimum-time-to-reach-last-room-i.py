#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dq = deque()
        dq.append([0, 0, 0])
        minimumTimeToReach = [[float("inf") for j in range(n)] for i in range(m)]
        minimumTimeToReach[0][0] = 0
        while dq:
            x, y, t = dq.popleft()
            neigs = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
            if t == minimumTimeToReach[x][y]:
                for nx, ny in neigs:
                    if 0 <= nx < m and 0 <= ny < n and minimumTimeToReach[nx][ny] > 1 + max(t, moveTime[nx][ny]) and moveTime[nx][ny] >= 0:
                        minimumTimeToReach[nx][ny] = 1 + max(t, moveTime[nx][ny])
                        dq.append([nx, ny, minimumTimeToReach[nx][ny]])
        return minimumTimeToReach[m - 1][n - 1]

# @lc code=end

