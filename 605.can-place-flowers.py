#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List


class Solution:
    '''
    Add an 0 before and after the flowerbed
    '''
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        consec = 1
        free = 0
        for i, pos in enumerate(flowerbed):
            if pos == 0:
                consec += 1
            else:
                if consec > 0:
                    free += (consec-1) // 2
                consec = 0
        if consec > 0:
            free += consec // 2       
        return free >= n
# @lc code=end

