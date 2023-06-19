#
# @lc app=leetcode id=1765 lang=python3
#
# [1765] Map of Highest Peak
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Any two adjacent cells must have an absolute height difference of at most 1
    We can get all the water cells and BFS from them. For each round, we assign its neighbor by its height + 1, assuming the neighbour is never assigned before. This way, we will never encounter a situation in which a land cell far away from one water cell but close to another water cell got assign the violating height 
    '''
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[0 for j in range(n)] for i in range(m)]
        dq, visited, current = deque(), set(), 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    dq.append((i, j))
                    visited.add((i, j))
        while dq:
            for j in range(len(dq)):
                x, y = dq.popleft()
                height[x][y] = current
                neigs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for nx, ny in neigs:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        dq.append((nx, ny))
            current += 1
        return height
# @lc code=end

