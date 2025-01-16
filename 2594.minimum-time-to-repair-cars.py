#
# @lc app=leetcode id=2594 lang=python3
#
# [2594] Minimum Time to Repair Cars
#

# @lc code=start
import math
from typing import List


class Solution:
    '''
    Binary search for the ans
    '''
    def numberOfCarsRepaired(self, ranks, t):
        result = 0
        for rank in ranks: result += int(math.sqrt(t // rank)) 
        return result

    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, min(ranks) * cars * cars + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.numberOfCarsRepaired(ranks, mid) < cars: l = mid + 1
            else: r = mid
        return l
    # @lc code=end
