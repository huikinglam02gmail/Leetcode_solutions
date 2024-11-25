#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS from the initial state and test if one can reach the target state    
    '''
    def board_to_string(self, board):
        string = ""
        for i in range(2):
            for j in range(3):
                string += str(board[i][j])
        return string
    
    def string_swap(self, s, i, j):
        new_s = ""
        for k in range(len(s)):
            if k == i: new_s += s[j]
            elif k == j: new_s += s[i]
            else: new_s += s[k]
        return new_s
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbours = {0: [1,3], 1: [0,2,4], 2: [1,5], 3: [0,4], 4: [1,3,5], 5: [2,4]}
        target = "123450"
        visited = set()
        dq = deque()
        board_string = self.board_to_string(board)
        dq.append(board_string)
        visited.add(board_string)
        count = 0
        while dq:
            for k in range(len(dq)):
                node = dq.popleft()
                if node == target: return count
                i = node.index('0')
                for j in neighbours[i]:
                    new_node = self.string_swap(node, i, j)
                    if new_node not in visited:
                        dq.append(new_node)
                        visited.add(new_node)
            count += 1
        return -1
# @lc code=end

