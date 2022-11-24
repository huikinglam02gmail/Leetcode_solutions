#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
import string
class Solution:
    # DFS  
    # Append "0" to the edge such that I can avoid edge effect codes
    # Then DFS from every point

    def dfs(self, row, col, word):
        if word == "":
            return True
        elif self.board[row][col] == word[0]:
            self.board[row][col] = "0"
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                if self.dfs(row + direction[0], col + direction[1], word[1:]):
                    return True
            self.board[row][col] = word[0]
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # Reject word being too long
        if len(word) > m*n:
            return False
        # Reject word with extra characters
        boardDict = {}
        wordDict = {}

        for c in string.ascii_letters:
            boardDict[c] = 0
            wordDict[c] = 0
        
        for i in range(m):
            for j in range(n):
                boardDict[board[i][j]] += 1
        
        for c in word:
            wordDict[c] += 1
        
        for c in string.ascii_letters:
            if wordDict[c] > boardDict[c]:
                return False
        
        if wordDict[word[0]] > wordDict[word[-1]]:
            word = word[::-1]

        self.board = [['0' for i in range(n+2)]]
        for row in board:
            self.board.append(["0"] + row + ["0"])
        self.board.append(['0' for i in range(n+2)])
        
        for i in range(1, len(self.board)-1):
            for j in range(1, len(self.board[0])-1):
                if self.dfs(i, j, word):
                    return True
        return False
# @lc code=end

