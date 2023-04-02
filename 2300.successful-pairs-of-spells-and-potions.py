#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Sort potions. For each spell, binary search for success // spells[i]
    '''
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        m = len(potions)
        for spell in spells:
            if success % spell == 0:
                result.append(m - bisect.bisect_left(potions, success // spell))
            else:
                result.append(m - bisect.bisect_right(potions, success // spell))
        return result               
        
# @lc code=end

