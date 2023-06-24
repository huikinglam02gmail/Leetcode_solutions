#
# @lc app=leetcode id=1776 lang=python3
#
# [1776] Car Fleet II
#

# @lc code=start
from typing import List


class Solution:
    '''
    According to the condition:
    Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.
    We know that the car being hit must be travelling slower than the one behind. After the collision, speed[i] does not change, but speed[j] becomes speed[i] < speed[j], j < i
    Therefore we wish to find out the car which cars[i] will collide with. The answer is the first car on the right which is slower than it is, or with collision time smaller than that of the calculated. A monotonic decreasing stack of collisionTimes would suffice. We should note that the condition to pop from the stack is either:
    1. The current car can never follow up with the considered car on the right
    2. The collision candidate has already bombarded before the collision with current car could take place.
    '''
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        result = []
        for pos, speed in cars[::-1]:
            while stack and (speed <= stack[-1][1] or (stack[-1][0] - pos) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()
            if not stack:
                stack.append([pos, speed, float("inf")])
                result.append(-1)
            else:
                collisionTime = (stack[-1][0] - pos) / (speed - stack[-1][1])
                stack.append([pos, speed, collisionTime])
                result.append(collisionTime)
        return reversed(result)
# @lc code=end

