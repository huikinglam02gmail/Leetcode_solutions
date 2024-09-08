#
# @lc app=leetcode id=2126 lang=python3
#
# [2126] Destroying Asteroids
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort asteroids
    Then do the exercise to destroy or die from left to right
    '''
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass >= asteroid: mass += asteroid
            else: return False
        return True
        
# @lc code=end

