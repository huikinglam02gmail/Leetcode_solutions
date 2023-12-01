#
# @lc app=leetcode id=1997 lang=python3
#
# [1997] First Day Where You Have Been in All the Rooms
#

# @lc code=start
from typing import List


class Solution:
    '''
    Notice the condition 0 <= nextVisit[i] <= i. So a path like 1 -> 5 -> 2 -> 1 can never happen
    To reach i, we must visited (i - 1) even times
    Let dp[i] =  the first day to reach room[i]
    for i > 0, dp[i] = dp[i - 1] + (# number of days to reach from i - 1 back to i - 1)
    In the second part, if nextVisit[i] = i (no back cycle), the time needed is 2: i - 1 -> i - 1 -> i
    If a cycle exist, the term is i - 1 -> nextVisit[i - 1] -> ... -> i - 1 -> i
    = 2 + dp[i - 1] - dp[nextVisit[i - 1]]
    '''
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = pow(10, 9) + 7
        n = len(nextVisit)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = 2 * dp[i - 1] + 2 - dp[nextVisit[i - 1]]
            dp[i] %= MOD
        return dp[-1]
# @lc code=end

