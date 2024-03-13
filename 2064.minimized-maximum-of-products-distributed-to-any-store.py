#
# @lc app=leetcode id=2064 lang=python3
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#

# @lc code=start
from typing import List


class Solution:
    '''
    Solve by binary search. The answer must be between 0 and max(quantities)
    To give at most x, quantities[i] has to be given to ceildiv(quantities[i], x) people.
    '''
    def ceildiv(self, a, b):
        return -(a // -b)

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        while l < r:
            mid =  l + (r - l) // 2
            numPeople = 0
            for q in quantities: numPeople += self.ceildiv(q, mid)
            if numPeople <= n:
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

