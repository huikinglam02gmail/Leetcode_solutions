#
# @lc app=leetcode id=2751 lang=python3
#
# [2751] Robot Collisions
#

# @lc code=start
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        data = []
        for i in range(n):
            if directions[i] == "R": data.append([positions[i], healths[i], 1, i])
            else: data.append([positions[i], healths[i], -1, i])
        data.sort()
        stack = []
        for pos, health, direction, ind in data:
            currentDestroyed = False
            newHealth = health
            while not currentDestroyed and stack and direction == -1 and stack[-1][2] == 1:
                if newHealth == stack[-1][1]:
                    currentDestroyed = True
                    stack.pop()
                elif newHealth < stack[-1][1]:
                    currentDestroyed = True
                    stack[-1][1] -= 1
                else:
                    stack.pop()
                    newHealth -= 1
            if not currentDestroyed:
                stack.append([pos, newHealth, direction, ind])
        stack.sort(key = lambda x: x[3])
        return [s[1] for s in stack]
        
# @lc code=end

