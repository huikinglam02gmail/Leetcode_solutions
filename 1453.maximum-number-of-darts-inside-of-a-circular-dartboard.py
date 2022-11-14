#
# @lc app=leetcode id=1453 lang=python3
#
# [1453] Maximum Number of Darts Inside of a Circular Dartboard
#

# @lc code=start
from math import acos, atan2, sqrt


class Solution:
    # From each dart, sweep a circle of radius r, with the dart lying on the circumference
    # Check for the other darts, their distance d: 
    # if d <= 2*r, that means an angular sweep from the first dart would include the second dart at some point.
    # For such second darts, we record their angle of entrance and leave the rotating circle
    # After going all such candidates, we sort the angles of entrance and leave
    # Record the maximum number of darts seen so far 
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        result = 0
        for x, y in darts:
            maxsofar, current = 1, 1
            angles = []
            for x1, y1 in darts:
                if x1 != x or y1 != y:
                    d = sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y))
                    if d <= 2*r:
                        theta = atan2(x1-x,y1-y)
                        delta = acos(d / 2 / r)
                        angles.append([theta - delta, 1])
                        angles.append([theta + delta, -1])
            angles.sort(key = lambda x: [x[0], -x[1]])

            for angle, state in angles:
                current += state
                maxsofar = max(maxsofar, current)
            result = max(result, maxsofar)
        return result
        
# @lc code=end

