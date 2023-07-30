#
# @lc app=leetcode id=335 lang=python3
#
# [335] Self Crossing
#

# @lc code=start
from typing import List


class Solution:
    '''
    Two points to note: 
    1. The Cartesian coordinate system is symmetric wih 90 degree rotations
    2. To cross a previous path with a future step, one can cross from left, right or from below
    '''
    def isSelfCrossing(self, distance: List[int]) -> bool:
        b = c = d = e = f = 0
        for a in distance:
            # cross from left
            if d > 0 and d >= b and a >= c:
                return True
            # cross from below
            if e > 0 and c <= a + e and b == d:
                return True
            # cross from the right
            if f > 0 and b <= d <= b + f and e <= c <= a + e:
                return True
            b, c, d, e, f = a, b, c, d, e 
        return False
# @lc code=end

