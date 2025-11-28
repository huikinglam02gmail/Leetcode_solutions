#
# @lc app=leetcode id=3752 lang=python3
#
# [3752] Lexicographically Smallest Negated Permutation that Sums to Target
#

# @lc code=start
from typing import List


class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        S = n * (n + 1) // 2
        if target < -S or target > S or (S - target) % 2: return []
        D = S - target
        result = [i for i in range(1, n + 1)]
        j = n - 1
        while D > 0 and j >= 0:
            if D >= 2 * (j + 1):
                result[j] = - (j + 1)
                D -= 2 * (j + 1)
            j -= 1
        return sorted(result)

# @lc code=end
