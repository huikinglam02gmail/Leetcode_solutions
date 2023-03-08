#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List


class Solution:
    '''
    Binary search for the answer
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1,  max(piles)
        while left < right:
            mid = (left + right) // 2
            if sum([- (pile // (- mid)) for pile in piles]) > h:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

