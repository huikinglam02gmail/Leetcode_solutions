#
# @lc app=leetcode id=913 lang=python3
#
# [913] Cat and Mouse
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Complicated problem which requires understanding of game theory
    Ridiculous if you are expected to solve it in an interview
    Main idea:
    We soon see that we need 3 variables to describe the states:
    (m, c, t)
    m = mouse's position (0-N)
    c = cat's position (0-N)
    t = whose turn (1: mouse; 2: cat)
    We know the final state of game:
    (i, i, t) = 2
    (0, i, t) = 1
    All else we need to find out
    The second key point is we can BFS in the reverse direction
    As we have well-defined final state, we can BFS into its parents
    We actually know well about which state can lead to the current state
    For example if graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    we know (0, i, 2) = 1. we then know from the graph,
    (2, i, 1) = 1, (5, i, 1) = 1, because it's the mouse's turn and they are going to pick the winning move. We can label these nodes and put into the queue to further BFS
    On the other hand, we also know (2,2,2) = 2. We then know that at (4,2,1), the mouse would never visit 2 because it will get caught. It might visit (3,2,2) instead to avoid getting caught
    To account for that game strategy, we record the outgoing degree for all states for both mouse and cat. Each time we arrive at such scenario, we decrease the degree of that state by 1. If the outgoing degree becomes 0, it means a mouse / cat getting into this state must lose (all paths outward does not lead to any wins)
    When the BFS is finished we just return the win state of mouse    
    '''

    
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        degree = [[[0 for k in range(3)] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][1] += len(graph[i])
                degree[i][j][2] += len(graph[j])
                if 0 in graph[j]:
                    degree[i][j][2] -= 1
        dq = deque()
        win = [[[0 for k in range(3)] for j in range(n)] for i in range(n)]
        for i in range(1, n):
            for k in range(1,3):
                win[0][i][k] = 1
                dq.append([0,i,k,1])
                win[i][i][k] = 2
                dq.append([i,i,k,2])

        while dq:
            m, c, t, w = dq.popleft()
            parents = []
            if t == 1:
                for parent in graph[c]:
                    if parent != 0:
                        parents.append([m, parent, 2])
            else:
                for parent in graph[m]:
                    parents.append([parent, c, 1])
            for mp, cp, tp in parents:
                if win[mp][cp][tp] == 0:
                    if tp == w: 
                        win[mp][cp][tp] = w
                        dq.append([mp, cp, tp, w])
                    else:
                        degree[mp][cp][tp] -= 1
                        if degree[mp][cp][tp] == 0:
                            win[mp][cp][tp] = w
                            dq.append([mp, cp, tp, w])
        return win[1][2][1]
# @lc code=end

