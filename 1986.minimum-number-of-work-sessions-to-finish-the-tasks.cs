/*
 * @lc app=leetcode id=1986 lang=csharp
 *
 * [1986] Minimum Number of Work Sessions to Finish the Tasks
 */

// @lc code=start
using System;

public class Solution {
    public int MinSessions(int[] tasks, int sessionTime) {
        int n = tasks.Length;
        int[,] dp = new int[1 << n, 2];
        for (int i = 0; i < (1 << n); i++) {
            dp[i, 0] = n;
            dp[i, 1] = 0;
        }
        dp[(1 << n) - 1, 0] = 1;
        dp[(1 << n) - 1, 1] = sessionTime;

        for (int mask = (1 << n) - 1; mask >= 0; mask--) {
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) {
                    int cntSession = dp[mask ^ (1 << i), 0];
                    int remainTime = dp[mask ^ (1 << i), 1];

                    if (tasks[i] <= remainTime) {
                        remainTime -= tasks[i];
                    } else {
                        cntSession += 1;
                        remainTime = sessionTime - tasks[i];
                    }

                    if (cntSession < dp[mask, 0] || (cntSession == dp[mask, 0] && remainTime > dp[mask, 1])) {
                        dp[mask, 0] = cntSession;
                        dp[mask, 1] = remainTime;
                    }
                }
            }
        }

        return dp[0, 0];
    }
}



// @lc code=end

