#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use the method introduced in Leetcode 59.
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        state, count, result = 0, 0, []
        i, j, m, n = 0, 0, len(matrix), len(matrix[0])
        while count < m * n:
            count += 1
            result.append(matrix[i][j])
            matrix[i][j] -= 201
            if count == m * n:
                break
            nxt = [[i, j + 1], [i + 1,j], [i, j - 1], [i - 1, j]]
            if nxt[state][0] < 0 or nxt[state][0] >= m or nxt[state][1] < 0 or nxt[state][1] >= n or matrix[nxt[state][0]][nxt[state][1]] < -100:
                state += 1
                state %= 4
            i, j = nxt[state]
        return result
# @lc code=end

