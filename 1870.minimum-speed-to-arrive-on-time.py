#
# @lc app=leetcode id=1870 lang=python3
#
# [1870] Minimum Speed to Arrive on Time
#

# @lc code=start
#
# @lc app=leetcode id=1870 lang=python3
#
# [1870] Minimum Speed to Arrive on Time
#

# @lc code=start
from typing import List


class Solution:
    '''
    Clearly a binary search problem. Just follow the instruction
    '''
    def timeToReach(self, speed):
        result = 0
        for i in range(len(self.dist) - 1):
            result += (self.dist[i] + speed - 1) // speed
        return result + self.dist[-1] / speed
    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        self.dist = dist
        self.hour = hour
        maxDist = max(self.dist)*100
        l, r = 1, maxDist + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.timeToReach(mid) > hour:
                l = mid + 1
            else:
                r = mid
        return -1 if l == maxDist + 1 else l
# @lc code=end

