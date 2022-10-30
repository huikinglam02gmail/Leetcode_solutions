#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
class Solution:
    # BFS will do the job
    # We BFS from the upper left corner.
    # state = (x,y,obstacles removed)
    # When we see an obstacle, we add one to obstacle
    # We also keep a hash table mapping coordinates to minimum obstacles to remove to reach the point
    # See if we can arrive at the the lower right
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n, steps, dq, visited = len(grid), len(grid[0]), 0, deque(), {}
        dq.append((0,0,0))
        visited[(0,0)] = 0
        while dq:
            for i in range(len(dq)):
                x, y, removed = dq.popleft()
                if x == m-1 and y == n-1:
                    return steps
                neigs = [(x-1, y), (x+1,y), (x,y-1),(x,y+1)]
                for xn, yn in neigs:
                    if xn >= 0 and yn >= 0 and xn < m and yn < n:
                        state = removed
                        if grid[xn][yn] == 1:
                            state += 1
                        if state <= k and ((xn, yn) not in visited or visited[(xn, yn)] > state):
                            dq.append((xn, yn, state))
                            visited[(xn,yn)] = state
            steps += 1
        return -1
# @lc code=end

