#
# @lc app=leetcode id=1610 lang=python3
#
# [1610] Maximum Number of Visible Points
#

# @lc code=start
import math
from typing import List


class Solution:
    # Firstly take care of the repeating points
    # Also, don't worry about the one sitting right at origin
    # Then compute the polar angle of each point by the math.atan2 method
    # Put all of them and 2pi + theta into a list, sort it and search by binary search to find how many points are inside theta and theta + angle
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        seen = {}
        for x, y in points:
            if (x, y) not in seen:
                seen[(x, y)] = 0
            seen[(x, y)] += 1
        relevant = []
        result = 0
        for x, y in seen.keys():
            if x != location[0] or y != location[1]:
                for j in range(seen[(x, y)]):
                    theta = math.atan2(y - location[1], x - location[0])
                    relevant.append(theta)
                    relevant.append(theta + 2*math.pi)
            else:
                result += seen[(x, y)]
        maxsofar = 0        
        if relevant:
            relevant.sort()
            ind = 0
            while relevant[ind] < math.pi:
                maxsofar = max(maxsofar, bisect.bisect_right(relevant, relevant[ind] + angle*math.pi/ 180) 
                - bisect.bisect_left(relevant, relevant[ind]))
                ind += 1
        return result + maxsofar
# @lc code=end

