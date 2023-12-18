#
# @lc app=leetcode id=2018 lang=python3
#
# [2018] Check if Word Can Be Placed In Crossword
#

# @lc code=start
from typing import List


class Solution:
    '''
    There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
    There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
    That means we just need to test for each point whether word can start from there
    '''
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word)
        proceedDirections = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#": continue # rule 1
                if board[i][j] != " " and board[i][j] != word[0]: continue # rule 2
                for k in range(4):
                    x, y, wordPtr = i, j, 0
                    xPrev, yPrev = x - proceedDirections[k][0], y - proceedDirections[k][1]
                    if 0 <= xPrev < m and 0 <= yPrev < n and board[xPrev][yPrev] != "#": continue # rule 3
                    while 0 <= x < m and 0 <= y < n and wordPtr < l:
                        if board[x][y] in [" ", word[wordPtr]]:
                            x += proceedDirections[k][0]
                            y += proceedDirections[k][1]
                            wordPtr += 1
                        else: break
                    if wordPtr < l: continue
                    if 0 <= x < m and 0 <= y < n and board[x][y] != "#": continue # rule 4
                    return True
        return False


# @lc code=end

