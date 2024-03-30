#
# @lc app=leetcode id=2079 lang=python3
#
# [2079] Watering Plants
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just simulation
    '''
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        curCapacity = capacity        
        for i, plant in enumerate(plants):
            if curCapacity < plant:
                result += 2 * i
                curCapacity = capacity
            curCapacity -= plant
            result += 1
        return result

# @lc code=end

