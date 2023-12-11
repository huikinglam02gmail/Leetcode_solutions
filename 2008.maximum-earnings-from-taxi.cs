/*
 * @lc app=leetcode id=2008 lang=csharp
 *
 * [2008] Maximum Earnings From Taxi
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Solve the problem with DP
    dp[i] = maximum number of dollars you can earn by picking up the passengers optimally when you are at i + 1.
    we look for dp[n - 1]
    dp[i] = max(dp[i - 1], dp[i - j] + i - j + tips)
    */
    public long MaxTaxiEarnings(int n, int[][] rides) {
        List<int[]>[] possibleEarnings = new List<int[]>[n];
        for (int i = 0; i < n; i++) {
            possibleEarnings[i] = new List<int[]>();
        }
        
        foreach (var ride in rides) {
            int s = ride[0] - 1;
            int e = ride[1] - 1;
            int t = ride[2];
            possibleEarnings[e].Add(new int[] { s, t });
        }
        
        long[] dp = new long[n];
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i - 1];
            foreach (var ride in possibleEarnings[i]) {
                int s = ride[0];
                int t = ride[1];
                dp[i] = Math.Max(dp[i], dp[s] + i - s + t);
            }
        }
        
        return dp[n - 1];
    }
}

// @lc code=end

