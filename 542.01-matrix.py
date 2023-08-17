#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS from all 0s
    Use mat as visited    
    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, steps, dq = len(mat), len(mat[0]), 0, deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i,j))
        result = [[0 for j in range(n)] for i in range(m)]
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                result[x][y] = steps
                neigs = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                for nx, ny in neigs:
                    if m > nx >= 0 <= ny < n and mat[nx][ny] == 1:
                        mat[nx][ny] = 0
                        dq.append((nx, ny))
            steps += 1
        return result
                        
            
# @lc code=end

