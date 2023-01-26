#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # Convert the board to an array
    # Then conduct BFS from 1 to n^2
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        arr, n = [], len(board)
        for i in range(n-1,-1,-1):
            if (n-1-i) % 2 == 0:
                arr += board[i]
            else:
                arr += board[i][::-1]
        dq, visited, steps = deque(), set(), 0
        dq.append(0)
        visited.add(0)
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node == n*n-1:
                    return steps
                for j in range(1,7):
                    nxt = node + j
                    if nxt < n*n:
                        if arr[node + j] != -1:
                            nxt = arr[node + j]-1
                        if nxt not in visited:
                            dq.append(nxt)
                            visited.add(nxt)
            steps += 1
        return -1
# @lc code=end

