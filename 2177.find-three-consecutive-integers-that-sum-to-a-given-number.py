#
# @lc app=leetcode id=2177 lang=python3
#
# [2177] Find Three Consecutive Integers That Sum to a Given Number
#

# @lc code=start
from typing import List


class Solution:
    '''
    a + a + 1 + a + 2 = num
    3 * a = num - 3
    edge case: num < 3: return []
    '''
    def sumOfThree(self, num: int) -> List[int]:
        if num >= 3 and (num - 3) % 3 == 0: return [(num - 3) // 3, (num - 3) // 3 + 1, (num - 3) // 3 + 2]
        elif num == 0: return [-1, 0, 1]
        return []
        
# @lc code=end

