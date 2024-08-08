#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#

# @lc code=start
from typing import List


class Solution:
    '''
    4 states: 0: going east, 1: going south, 2: going west, 3: going north
    Look at how much to move:
    0: 1 step, 1: 1 step, 2: 2 steps, 3: 2 steps; 4%4 = 0: 3 steps...
    steps % 4: steps // 2 + 1 steps
    just keep track of it x, y     
    '''
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        steps, result = 0, []
        x, y = rStart, cStart
        while len(result) < rows * cols:
            for j in range(1 + steps // 2):
                if x >= 0 and x < rows and y >= 0 and y < cols: result.append([x, y])
                if steps % 4 == 0:  y += 1
                elif steps % 4 == 1: x += 1
                elif steps % 4 == 2: y -= 1
                else:  x -= 1
            steps += 1
        return result
    # @lc code=end

