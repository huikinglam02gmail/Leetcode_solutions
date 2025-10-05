#
# @lc app=leetcode id=3697 lang=python3
#
# [3697] Compute Decimal Representation
#

# @lc code=start
from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        while n > 0:
            result.append(n % 10)
            n //= 10
        result2 = []
        for i, num in enumerate(result):
            if num > 0: result2.append(num * pow(10, i))
        return result2[::-1]
# @lc code=end

