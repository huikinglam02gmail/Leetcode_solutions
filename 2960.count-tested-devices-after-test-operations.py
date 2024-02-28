#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just follow instruction
    '''
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = 0
        deducted = 0
        i = 0
        while i < len(batteryPercentages):
            if batteryPercentages[i] - deducted > 0:
                result += 1
                deducted += 1
            i += 1
        return result
        
# @lc code=end

