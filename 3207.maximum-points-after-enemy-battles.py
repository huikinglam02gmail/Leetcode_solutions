#
# @lc app=leetcode id=3207 lang=python3
#
# [3207] Maximum Points After Enemy Battles
#

from collections import deque
from typing import List

# @lc code=start
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        points = 0
        dq = deque(enemyEnergies)
        while dq and currentEnergy >= dq[0]:
            points += currentEnergy // dq[0]
            currentEnergy %= dq[0]
            while dq and currentEnergy < dq[0] and points > 0:
                currentEnergy += dq.pop()
        return points
        

# @lc code=end
