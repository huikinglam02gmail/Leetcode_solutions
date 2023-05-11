#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Try to do it by imposing some rules
    state = 0: East, 1: South, 2: West, 3: North
    We let the cursor to go around the matrix until n*n elements are filled
    When the next step of the cursor is going out of bound or the point is already written, we turn 90 degress   
    '''

    def generateMatrix(self, n: int) -> List[List[int]]:
        state, count, result = 0, 0, [[0 for i in range(n)] for j in range(n)]
        i, j = 0, 0
        while count < n*n:
            count += 1
            result[i][j] = count
            if count == n*n:
                break
            nxt = [[i, j+1], [i+1,j], [i, j-1], [i-1,j]]
            if nxt[state][0] < 0 or nxt[state][0] >= n or nxt[state][1] < 0 or nxt[state][1] >= n or result[nxt[state][0]][nxt[state][1]] > 0:
                state += 1
                state %= 4
            i, j = nxt[state]
        return result
# @lc code=end

