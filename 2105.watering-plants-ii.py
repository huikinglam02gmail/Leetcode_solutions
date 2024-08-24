#
# @lc app=leetcode id=2105 lang=python3
#
# [2105] Watering Plants II
#

# @lc code=start
from typing import List


class Solution:
    '''
    just simulate
    '''
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        result, n = 0, len(plants)
        A, B = capacityA, capacityB
        i, j = 0, n - 1
        while i < j:
            if A < plants[i]:
                A = capacityA
                result += 1
            if B < plants[j]:
                B = capacityB
                result += 1
            A -= plants[i]
            B -= plants[j]
            i += 1
            j -= 1
        if i == j and max(A, B) < plants[i]: result += 1 
        return result
# @lc code=end

