#
# @lc app=leetcode id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Construct a minimum distance matrix, from each 1, propagate by BFS to fill the entire minimum distance matrix.
    Then binary search for the answer between [0, 2 * n - 2]. We BFS from (0, 0) to (n - 1, n - 1), and cannot enter (i, j) if minD[i][j] < mid
    '''
    def canReach(self, thres):
        dq = deque()
        visited = [[False for j in range(self.n)] for i in range(self.n)]
        if self.minD[0][0] >= thres:
            dq.append((0, 0))
            visited[0][0] = True
        while dq:
            x, y = dq.popleft()
            if x == self.n - 1 and y == self.n - 1: return True
            neigs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nx, ny in neigs:
                if 0 <= nx < self.n and 0 <= ny < self.n and not visited[nx][ny] and self.minD[nx][ny] >= thres:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.minD = [[float("Inf") for j in range(self.n)] for i in range(self.n)]
        dq = deque()
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 1: 
                    dq.append((i, j))
                    self.minD[i][j] = 0
        steps = 1
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                neigs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                for nx, ny in neigs:
                    if 0 <= nx < self.n and 0 <= ny < self.n and self.minD[nx][ny] == float("Inf"):
                        self.minD[nx][ny] = steps
                        dq.append((nx, ny))
            steps += 1
        
        l, r = 0, 2 * self.n - 1
        while l < r:
            mid = l + (r - l) // 2
            canReach = self.canReach(mid)
            if canReach:
                l = mid + 1
            else:
                r = mid
        return l - 1

# @lc code=end

