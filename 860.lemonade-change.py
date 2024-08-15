#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
from typing import List


class Solution:
    '''
    Simulate the process    
    '''
    def lemonadeChange(self, bills: List[int]) -> bool:
        reserve = [0,0,0]
        for i in bills:
            if i == 10:
                if reserve[0] < 1: return False
                else:
                    reserve[1] += 1
                    reserve[0] -= 1
            elif i == 20:
                if reserve[1] < 1 or reserve[0] < 1:
                    if reserve[0] < 3: return False
                    else:
                        reserve[0] -= 3
                        reserve[2] += 1
                else:
                    reserve[1] -= 1
                    reserve[0] -= 1
                    reserve[2] += 1
            else:
                reserve[0] += 1
        return True
# @lc code=end

