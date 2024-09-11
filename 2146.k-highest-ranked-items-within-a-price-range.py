#
# @lc app=leetcode id=2146 lang=python3
#
# [2146] K Highest Ranked Items Within a Price Range
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    '''
    Distance can be computed by BFS from start
    Arriving at a point (i, j), ask if pricing[0] <= grid[i][j] <= pricing[1]
    If so, place (d, grid[i][j], i, j) into a heap, maintain the heap to be at most size k
    When visited the whole grid, pop items from heap and return
    '''
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        steps = 0
        m = len(grid)
        n = len(grid[0])
        dq = deque()
        dq.append(start)
        heap = []
        if pricing[0] <= grid[start[0]][start[1]] <= pricing[1]: heapq.heappush(heap, [- steps, - grid[start[0]][start[1]], - start[0], - start[1]])
        grid[start[0]][start[1]] = 0
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                neigs = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
                for xN, yN in neigs:
                    if 0 <= xN < m and 0 <= yN < n and grid[xN][yN] > 0: 
                        dq.append([xN, yN])
                        if pricing[0] <= grid[xN][yN] <= pricing[1]: 
                            heapq.heappush(heap, [- steps - 1, - grid[xN][yN], - xN, -yN])
                            while len(heap) > k: heapq.heappop(heap)                      
                        grid[xN][yN] = 0
            steps += 1
        result = []
        while heap:
            d, p, x, y = heapq.heappop(heap)
            result.append([- x, - y])
        return reversed(result)

# @lc code=end
