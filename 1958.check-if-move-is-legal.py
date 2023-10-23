#
# @lc app=leetcode id=1958 lang=python3
#
# [1958] Check if Move is Legal
#

# @lc code=start
from typing import List


class Solution:
    '''
    Check in this manner:
    In eight directions, go forward with the opposite color until it got stopped by color
    '''
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        steps = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        opp = {'B' : 'W', 'W': 'B'}
        for i in range(8):
            x, y = rMove, cMove
            countDiff = 0
            while 0 <= x + steps[i][0] < m and 0 <= y + steps[i][1] < n:
                x += steps[i][0]
                y += steps[i][1]
                if board[x][y] == opp[color]: 
                    countDiff += 1
                elif board[x][y] == color and countDiff > 0:
                    return True
                else:
                    break
        return False
# @lc code=end

