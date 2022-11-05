#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode(object):    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    # Backtracking on a Trie
    # First build the Trie according to words
    # Then DFS from each grid point to start for 10 steps
    def dfs(self, x, y, node, word):
        if node.isEnd and word not in self.result:
            self.result.add(word)
            self.charWordStart[ord(word[0])-ord('a')] -= 1
            
        candidates = [(x-1, y), (x+1, y), (x,y-1), (x,y+1)]
        for nx, ny in candidates:
            if len(self.board) > nx >= 0 <= ny < len(self.board[0]) and self.board[nx][ny] in node.children:
                c = self.board[nx][ny]
                self.board[nx][ny] = 'X'
                self.dfs(nx, ny, node.children[c], word + c)
                self.board[nx][ny] = c
                
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Find what is available on the board
        self.board = board
        charBoard, m, n = [0]*26, len(board), len(board[0])
        for row in board:
            for c in row:
                charBoard[ord(c)-ord('a')] += 1
        
        # Construct the Trie
        root = TrieNode()
        self.charWordStart = [0]*26
        for word in words:
            charWord = [0]*26
            for c in word:
                charWord[ord(c)-ord('a')] += 1
            if all([charWord[i] <= charBoard[i] for i in range(26)]):
                node = root
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode()                
                    node = node.children[c]
                node.isEnd = True
                self.charWordStart[ord(word[0])-ord('a')] += 1 
        
        self.result = set()        
        # DFS
        for i in range(m):
            for j in range(n):
                c = self.board[i][j]
                if c in root.children and self.charWordStart[ord(c)-ord('a')] > 0:
                    self.board[i][j] = 'X'
                    self.dfs(i,j,root.children[c],c)
                    self.board[i][j] = c
        return self.result
# @lc code=end

