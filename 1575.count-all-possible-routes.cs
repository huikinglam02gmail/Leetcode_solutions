/*
 * @lc app=leetcode id=1575 lang=csharp
 *
 * [1575] Count All Possible Routes
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int CountRoutes(int[] locations, int start, int fin, int fuel) {
        int n = locations.Length;
        long MOD = 1000000007;
        int[][] cost = new int[n][];
        for (int i = 0; i < n; i++) {
            cost[i] = new int[n];
            for (int j = 0; j < n; j++) {
                cost[i][j] = Math.Abs(locations[i] - locations[j]);
            }
        }

        long[][] dp = new long[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new long[fuel + 1];
        }

        dp[start][fuel] = 1;

        for (int f = fuel; f >= 0; f--) {
            for (int i = 0; i < n; i++) {
                if (dp[i][f] > 0) {
                    for (int j = 0; j < n; j++) {
                        if (j != i && f - cost[i][j] >= 0) {
                            dp[j][f - cost[i][j]] += dp[i][f];
                            dp[j][f - cost[i][j]] %= MOD;
                        }
                    }
                }
            }
        }

        long sum = 0;
        for (int i = 0; i <= fuel; i++)
        {
            sum += dp[fin][i];
            sum %= MOD;
        }

        return Convert.ToInt32(sum);
    }
}

// @lc code=end

