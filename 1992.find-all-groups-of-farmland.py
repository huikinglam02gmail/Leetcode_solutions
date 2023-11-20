#
# @lc app=leetcode id=1992 lang=python3
#
# [1992] Find All Groups of Farmland
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Groups of farmland are rectangular in shape.
    So just BFS from potential top left corner and if cannot find right and bottom neighbour, that's the end
    '''
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n, result = len(land), len(land[0]), []
        visited = [[land[i][j] == 0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    dq = deque()
                    dq.append([i, j, i, j])
                    visited[i][j] = True
                    while dq:
                        x1, y1, x2, y2 = dq.popleft()
                        if (x2 == m - 1 or land[x2 + 1][y2] == 0) and (y2 == n - 1 or land[x2][y2 + 1] == 0):
                                result.append([x1, y1, x2, y2])
                        else:
                            if x2 + 1 < m and not visited[x2 + 1][y2]:
                                visited[x2 + 1][y2] = True
                                dq.append([x1, y1, x2 + 1, y2])
                            if y2 + 1 < n and not visited[x2][y2 + 1]:
                                visited[x2][y2 + 1] = True
                                dq.append([x1, y1, x2, y2 + 1])
        return result
# @lc code=end

