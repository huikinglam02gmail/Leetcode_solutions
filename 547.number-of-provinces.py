#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS to find connected components    
    '''
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dq, visited = deque(), set()
        province, n = 0, len(isConnected)
        for i in range(n):
            if i not in visited:
                dq.append(i)
                visited.add(i)
                province += 1
                while dq:
                    x = dq.popleft()
                    for j in range(n):
                        if isConnected[x][j] == 1 and j not in visited:
                            dq.append(j)
                            visited.add(j)         
        return province        
# @lc code=end

