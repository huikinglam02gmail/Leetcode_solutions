#
# @lc app=leetcode id=2257 lang=python3
#
# [2257] Count Unguarded Cells in the Grid
#

# @lc code=start
from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unGuarded = [[True for j in range(n)] for i in range(m)]
        wallSet = set()
        for wallX, wallY in walls: 
            unGuarded[wallX][wallY] = False
            wallSet.add((wallX, wallY))
        for guardX, guardY in guards:
            unGuarded[guardX][guardY] = False
            wallSet.add((guardX, guardY))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for guardX, guardY in guards:
            for i in range(4):
                x, y = guardX + directions[i][0], guardY + directions[i][1]
                while 0 <= x < m and 0 <= y < n and (x, y) not in wallSet:
                    unGuarded[x][y] = False
                    x += directions[i][0]
                    y += directions[i][1]
        count = 0
        for i in range(m):
            for j in range(n):
                if unGuarded[i][j]: count += 1
        return count
                
            
# @lc code=end

