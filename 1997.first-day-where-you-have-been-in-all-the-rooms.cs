/*
 * @lc app=leetcode id=1997 lang=csharp
 *
 * [1997] First Day Where You Have Been in All the Rooms
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FirstDayBeenInAllRooms(int[] nextVisit) {
        long MOD = 1000000007;
        int n = nextVisit.Length;
        long[] dp = new long[n];

        for (int i = 1; i < n; i++) {
            dp[i] = (2 * dp[i - 1] + 2 - dp[nextVisit[i - 1]] + MOD) % MOD;
        }

        return Convert.ToInt32(dp[n - 1]);
    }
}

// @lc code=end

