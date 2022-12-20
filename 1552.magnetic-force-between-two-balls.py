#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
from typing import List


class Solution:
    # Rather than trying to place m balls into different configurations to optimize
    # We should change our perspective, and ask:
    # What is the maximum number of balls we can put inside the given baskets such that the minimum distance between two balls is at least d? f(d)
    # We see that with larger d, f is nonincreasing because we are limited by the separation constraint
    # Therefore, we can binary search for d, such that f(d) = m and f(d + 1) < m
    
    def ballCount(self, d):
        curr, ans = - float('inf'), 0
        for i in range(len(self.Position)):
            if self.Position[i] - curr >= d:
                curr = self.Position[i]
                ans += 1
        return ans

    def maxDistance(self, position: List[int], m: int) -> int:
        self.Position = sorted(position)        
        l, r = 1, self.Position[-1] - self.Position[0]
        while l < r:
            mid = r - (r - l) // 2
            if self.ballCount(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
# @lc code=end
