#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1  # Do not have enough flowers
        else:
            # Binary search on the minimal days such that I can make m bouquets
            left = min(bloomDay)
            right = max(bloomDay) + 1
            while left < right:
                mid = left + (right - left) // 2
                # count how many bouquets I can make
                bouquets = 0
                flowers = 0
                for bloom in bloomDay:
                    if bloom > mid:
                        flowers = 0
                    else:
                        bouquets += (flowers + 1) // k
                        flowers = (flowers + 1) % k
                
                if bouquets >= m:
                    right = mid
                else:
                    left = mid + 1
            return left        
# @lc code=end

