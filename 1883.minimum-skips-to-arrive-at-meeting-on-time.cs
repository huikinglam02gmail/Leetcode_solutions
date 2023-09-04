/*
 * @lc app=leetcode id=1883 lang=csharp
 *
 * [1883] Minimum Skips to Arrive at Meeting On Time
 */

// @lc code=start
using System;

public class Solution {
    public int MinSkips(int[] dist, int speed, int hoursBefore) {
        int n = dist.Length;

        int CeilDiv(int a, int b) {
            return (a + b - 1) / b;
        }

        int[,] dp = new int[n, n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i, j] = -1;
            }
        }

        int DP(int i, int j) {
            if (j < 0) return int.MaxValue;
            if (i == n) return 0;
            if (dp[i, j] != -1) return dp[i, j];
            
            int result = dist[i] + Math.Min(DP(i + 1, j - 1), CeilDiv(DP(i + 1, j), speed) * speed);
            dp[i, j] = result;
            return result;
        }

        if (dist.Sum() > speed * hoursBefore) {
            return -1;
        }

        for (int i = 0; i < n; i++) {
            if (DP(0, i) <= speed * hoursBefore) {
                return i;
            }
        }

        return -1;
    }
}

// @lc code=end

