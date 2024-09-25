#
# @lc app=leetcode id=2178 lang=python3
#
# [2178] Maximum Split of Positive Even Integers
#

# @lc code=start
from typing import List


class Solution:
    '''
    if finalSum is odd, return []
    Then try to use 2, 4, 6, ... , until cur + last + 2 > finalSum
    '''
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result = []
        if finalSum % 2 == 0:
            current = 0
            last = 0
            while current + last + 2 <= finalSum:
                last += 2
                result.append(last)
                current += last
            if current < finalSum:
                current -= result.pop()
                result.append(finalSum - current)
        return result

        
# @lc code=end
