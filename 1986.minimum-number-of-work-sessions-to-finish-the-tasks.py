#
# @lc app=leetcode id=1986 lang=python3
#
# [1986] Minimum Number of Work Sessions to Finish the Tasks
#

# @lc code=start
from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        dp = [[n, 0] for i in range(1 << n)]
        dp[-1] = [1, sessionTime]
        for mask in range(1 << n - 1, -1, -1):
            for i in range(n):
                if mask & (1 << i) == 0:
                    cntSession, remainTime = dp[mask ^ (1 << i)]
                    if tasks[i] <= remainTime:
                        remainTime -= tasks[i]
                    else:
                        cntSession += 1
                        remainTime = sessionTime - tasks[i]
                    if cntSession < dp[mask][0] or (cntSession == dp[mask][0] and remainTime > dp[mask][1]):
                        dp[mask] = [cntSession, remainTime]
        return dp[0][0]
# @lc code=end

