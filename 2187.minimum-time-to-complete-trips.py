#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
from typing import List


class Solution:
    '''
    Solve by binary search. Assume the answer is t, just add up all time[i] // t, find the first t in which sum >= totalTrips
    '''
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, max(time) * totalTrips
        while left < right:
            mid = left + (right - left) // 2
            ans = 0
            for t in time:
                ans += mid // t
            if ans < totalTrips:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

