#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start
from typing import List


class Solution:
    '''
    Remove all rows with "0" * n
    Then for two consecutive rows, add multiples of counts together
    '''
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, result = 0, 0
        for row in bank:
            cur = row.count('1')
            if not cur: continue
            result += prev * cur
            prev = cur
        return result

# @lc code=end

