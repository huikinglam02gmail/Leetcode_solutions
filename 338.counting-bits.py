#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from typing import List


class Solution:
    '''
    Because the number we have is increasing one by one, we easily arrange into this manner:
    [0, 2^0, 2^1, 2^1 + 2^0, ....]
    Just keep track of power of two
    '''
    def countBits(self, n: int) -> List[int]:
        cur = 0
        result = [0]
        for i in range(1, n + 1):
            if i > (1 << cur):
                cur += 1
            result.append(result[i - (1 << cur)] + 1)
        return result
# @lc code=end

