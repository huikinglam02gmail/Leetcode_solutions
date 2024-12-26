#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
from typing import List


class Solution:
    '''
    Simple binary search
    '''
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies) + 1
        while l < r:
            mid = l + (r - l) // 2
            result = 0
            for candy in candies: result += candy // mid
            if result >= k: l = mid + 1
            else: r = mid
        return l - 1
# @lc code=end

