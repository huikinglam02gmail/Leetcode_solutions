#
# @lc app=leetcode id=1655 lang=python3
#
# [1655] Distribute Repeating Integers
#

# @lc code=start
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    """
    There are only 10 customers and 50 types of nums. So we can use bitmask such that bitmask[j] = 1 to represent customer[j] is satisfied.
    
    We prepare for each possible submask, the sum of quantities each satisfied customer want.

    Then we go on to dfs. By incrementing mask from 0 to 1 << m - 1, we ask if the current item can satisfy all the customers in the current submask. If so, we also ask if the remainder not included in submask can be satisfied by the rest of items.

    """ 
    @lru_cache(None)
    def recurse(self, i, mask):        
        if mask == 0:
            return True
        if i == len(self.a):
            return False
        submask = mask
        while submask:
            if self.maskSum[submask] <= self.a[i] and self.recurse(i+1, mask ^ submask):
                return True
            submask = (submask-1) & mask
        return self.recurse(i+1, mask) 

    def canDistribute(self, nums: List[int], customers: List[int]) -> bool:
        c = Counter(nums)
        self.a = list(c.values())
        m = len(customers)
        self.maskSum = [0]*(1 << m)
        for mask in range(1 << m):
            for i in range(m):
                if (1 << i) & mask:
                    self.maskSum[mask] += customers[i]           
        return self.recurse(0, (1 << m) - 1 )
        
                    
# @lc code=end

