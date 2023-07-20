#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use a stack to maintain the preexisting asteroids
    One important point is the negative ones appearing left of the positive ones will never collide, so will be ignored
    I used a collision_ended marker to indicate if any collision between an old positive asteroid in the stack and a new negative asteroid has been accounted for. Note that I only turn it True when the incoming asteroid is larger than or equal to the incoming asteroid.    
    '''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                collision_ended = False
                while stack and (stack[-1] >= 0 and asteroid < 0) and not collision_ended:
                    old = stack.pop()
                    collision_ended = old + asteroid >= 0
                    if old + asteroid > 0:
                        stack.append(old)
                if not collision_ended:
                    stack.append(asteroid)
        return stack
# @lc code=end

