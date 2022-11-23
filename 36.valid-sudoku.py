#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hash_set = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in hash_set:
                        return False
                    else:
                        hash_set.add(board[i][j])
        for i in range(len(board[0])):
            hash_set = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in hash_set:
                        return False
                    else:
                        hash_set.add(board[j][i])
        for k in range(0,9,3):
            for l in range(0,9,3):
                hash_set = set()
                for i in range(k,k+3):
                    for j in range(l,l+3):
                        if board[i][j] != ".":
                            if board[i][j] in hash_set:
                                return False
                            else:
                                hash_set.add(board[i][j])
        return True 
# @lc code=end

