#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#

# @lc code=start
from typing import List


class Solution:
    # Make a hash table of modulo k
    # Then find if all count[x] == count[k - x]
    # Special case x = 0: check if it is even
    def canArrange(self, arr: List[int], k: int) -> bool:
        modulo = [0]*k
        for num in arr:
            modulo[num % k] += 1
        if modulo[0] % 2 != 0:
            return False
        for i in range(1, k // 2 + 1):
            if i == k - i and modulo[i] % 2 != 0:
                return False
            elif i != k - i and modulo[i] != modulo[k-i]:
                return False
        return True

# @lc code=end

