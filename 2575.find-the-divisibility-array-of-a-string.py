#
# @lc app=leetcode id=2575 lang=python3
#
# [2575] Find the Divisibility Array of a String
#

# @lc code=start
from typing import List


class Solution:
    '''
    Suppose word[:i] = x = a[i - 1] * m + b[i - 1]
    word[: i + 1] = 10 * x + int(word[i]) = 10 * a[i - 1] * m + 10 * b[i - 1] + int(word[i])
    b[i] = (10 * b[i - 1] + int(word[i])) % m
    '''
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        b = 0
        result = []
        for c in word:
            b = 10 * b + int(c)
            b %= m
            if b == 0: result.append(1)
            else: result.append(0)
        return result
# @lc code=end

