#
# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#

# @lc code=start
from collections import deque
from typing import Deque, List


class Solution:
    '''
    This is not an ordinary BFS problem
    But it's rather like a travelling salesman problem
    Similar problem: Leetcode 847. Shortest Path Visiting All Nodes
    The goal of the operator is to get all the keys as soon as possible.
    In the process, one might choose to open locks or choose to return (a valid action).
    To avoid getting into cycles, we denote whether a certain key is in possession as the state
    '''

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n, keystring = len(grid), len(grid[0]), ""
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    keystring += grid[i][j]
                elif grid[i][j] == "@":
                    start = [i,j]
        keystring = "".join(sorted(keystring))
        key_hash = {}
        for i, c in enumerate(keystring):
            key_hash[c] = i
            
        dq, visited, steps = deque(), set(), 0
        state = start + [0]
        dq.append(state)
        visited.add(tuple(state))
        neigs = [[0,1],[0,-1],[1,0],[-1,0]]
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node[2] == (1 << len(keystring)) - 1:
                    return steps
                for neig in neigs:
                    new_node = [node[0] + neig[0], node[1] + neig[1]]
                    if 0 <= new_node[0] < m and 0 <= new_node[1] < n:
                        c =  grid[new_node[0]][new_node[1]]
                        if c == "." or c == "@" or (c.isupper() and node[2] & (1 << key_hash[c.lower()]) != 0): 
                            if tuple(new_node + [node[2]]) not in visited:
                                dq.append(new_node + [node[2]])
                                visited.add(tuple(new_node + [node[2]]))
                        elif c.islower():
                            if node[2] & (1 << key_hash[c]) == 0:
                                new_state = node[2] ^ (1 << key_hash[c]) 
                            else:
                                new_state = node[2]
                            if tuple(new_node + [new_state]) not in visited:
                                dq.append(new_node + [new_state])
                                visited.add(tuple(new_node + [new_state]))
            steps += 1
        return -1
                            
# @lc code=end

