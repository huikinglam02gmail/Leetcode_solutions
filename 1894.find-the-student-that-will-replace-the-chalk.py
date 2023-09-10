#
# @lc app=leetcode id=1894 lang=python3
#
# [1894] Find the Student that Will Replace the Chalk
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    prepare prefix sum
    return the bisectRight(prefix, k % prefix[-1])
    '''
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = [0]
        for num in chalk:
            prefix.append(prefix[-1] + num)
        return bisect.bisect_right(prefix, k % prefix[-1]) - 1
# @lc code=end

