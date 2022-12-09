#
# @lc app=leetcode id=1515 lang=python3
#
# [1515] Best Position for a Service Centre
#

# @lc code=start
import math
from typing import List


class Solution:
    # Geometric median problem
    # Adopt a more simple approach than well known methods that converges faster
    # Each step we try to move in 4 directions with defined step to check if the distance function will increase
    # If we find a lower point, we move over and repeat
    # else, we shrink the limit by 2
    def euclidean(self, x, y):
        distance = 0
        for px, py in self.pos:
            distance += math.sqrt((x - px)*(x - px) + (y - py)*(y - py))
        return distance

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        self.pos = positions
        n = len(self.pos)
        step = 100
        limit = 0.000001
        x, y = sum([x[0] for x in self.pos]) / n,  sum([x[1] for x in self.pos]) / n
        current = self.euclidean(x, y)

        while step > limit:
            nxtDistance = []
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx = x + dx*step
                ny = y + dy*step
                nxtDistance.append([self.euclidean(nx, ny), nx, ny])
            nxtDistance.sort()
            if nxtDistance[0][0] < current:
                current, x, y = nxtDistance[0]
            else:
                step /= 2
        return current
# @lc code=end

