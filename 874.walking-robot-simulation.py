#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
from typing import List


class Solution:
    '''
    Save the obstacles as hash set
    For the robot, we specify its state by three parameters:
    [x, y, dir]; dir: 0: north, 1: east, 2: south, 3: west
    therefore, if -2: 0 -> 3, 1 -> 0,.. etc. = (dir + 3) % 4
    if -1: (dir + 5) % 4    
    '''
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        result = 0
        state = [0, 0, 0]
        obstacles_set = set()
        for obstacle in obstacles: obstacles_set.add(tuple(obstacle))
        for command in commands:
            if command == -1: state[2] = (state[2] + 5) % 4
            elif command == -2: state[2] = (state[2] + 3) % 4
            else:
                for i in range(command):
                    if state[2] == 0: nxt = [state[0], state[1] + 1]
                    elif state[2] == 1: nxt = [state[0] + 1, state[1]]
                    elif state[2] == 2: nxt = [state[0], state[1] - 1]
                    else: nxt = [state[0] - 1, state[1]]
                    if tuple(nxt) not in obstacles_set:
                        state[0] = nxt[0]
                        state[1] = nxt[1]
                        result = max(result, state[0]*state[0] + state[1]*state[1])
        return result
# @lc code=end

