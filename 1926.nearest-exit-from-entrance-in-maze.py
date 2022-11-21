#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
class Solution:
    # BFS from entrance
    # To avoid edge case of entrance being on the edge, we can stop BFS in the neighbour search part
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dq, steps, m, n = deque(), 0, len(maze), len(maze[0])
        dq.append(entrance)
        maze[entrance[0]][entrance[1]] = "+"
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                neigs = [[x+1,y], [x-1,y], [x,y+1], [x, y-1]]
                for xn, yn in neigs:
                    if m > xn >= 0 <= yn < n and maze[xn][yn] == ".":
                        if xn == 0 or yn == 0 or xn == m-1 or yn == n-1:
                            return steps + 1
                        dq.append([xn, yn])
                        maze[xn][yn] = "+"
            steps += 1
        return -1
# @lc code=end

