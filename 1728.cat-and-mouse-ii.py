#
# @lc app=leetcode id=1728 lang=python3
#
# [1728] Cat and Mouse II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    '''
    Similar to Leetcode 913 except harder. We first build the graph. The state will be identified by (mx, my, cx, cy, lastMoveAnimal). We keep states which for sure will lead to a mouse win in the queue. We also use a cache to store the current status of the state: cache(state) = 2 if cat catch mouse or cat reaches food. cache(state) = 1 is mouse can sure win if this state, cache(state) = 0 it is uncertain.
    '''
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        mouse = [-1, -1]
        cat = [-1, -1]
        food = [-1, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'M':
                    mouse = [i, j]
                elif grid[i][j] == 'F':
                    food = [i, j]
                elif grid[i][j] == 'C':
                    cat = [i, j]
        
        def prevPositions(x, y, jump):
            result = set()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                for i in range(jump + 1):
                    if not (0 <= x + dx * i < m and 0 <= y + dy * i < n) or grid[x + dx * i][y + dy * i] == '#':
                        break
                    result.add((x + dx * i, y + dy * i))
            return result

        cache =  defaultdict(int)
        GraphMouse = {}
        GraphCat = {}
        dq = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '#':
                    continue
                GraphMouse[(r, c)] = prevPositions(r, c, mouseJump)
                GraphCat[(r, c)] = prevPositions(r, c, catJump)
                for turn in range(2):
                    cache[(r, c, r, c, turn)] = 2
                    cache[(r, c, food[0], food[1], turn)] = 2
                    cache[(food[0], food[1], r, c, turn)] = 1
                    dq.append((food[0], food[1], r, c, turn))
        
        while dq:
            mx, my, cx, cy, turn = dq.popleft()
            if turn == 0:
                for mxLast, myLast in GraphMouse[(mx, my)]:
                    lastState = (mxLast, myLast, cx, cy, 1)
                    if cache[lastState] > 0:
                        continue
                    else:
                        cache[lastState] = 1
                        dq.append(lastState)
            else:
                for cxLast, cyLast in GraphCat[(cx, cy)]:
                    lastState = (mx, my, cxLast, cyLast, 0)
                    if cache[lastState] > 0:
                        continue
                    else:
                        cache[lastState] -= 1
                        if cache[lastState] == -len(GraphCat[(cxLast, cyLast)]):
                            cache[lastState] = 1
                            dq.append(lastState)
        
        return cache[(mouse[0], mouse[1], cat[0], cat[1], 1)] == 1
# @lc code=end
