#
# @lc app=leetcode id=1751 lang=python3
#
# [1751] Maximum Number of Events That Can Be Attended II
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    '''
    DP problem. First sort events by starttime
    dp(i, j) = maximum sum of values that you can receive by attending events[i:], whereas you have j events left
    dp(i, j) = max(dp(i + 1, j), events[i][2] + dp(next available index, j - 1))
    skip event i or attend event i
    if j == 0: dp(i, j) = 0
    We are looking for dp(0, k)
    '''
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[0 for j in range(k + 1)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                if i < n - 1:
                    dp[i][j] = dp[i + 1][j]
                nxtInd = bisect.bisect_right(events, events[i][1], key = itemgetter(0))
                dp[i][j] = max(dp[i][j], events[i][2] + (dp[nxtInd][j - 1] if nxtInd < n else 0))
        return dp[0][k]

# @lc code=end

