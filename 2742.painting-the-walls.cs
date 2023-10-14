/*
 * @lc app=leetcode id=2742 lang=csharp
 *
 * [2742] Painting the Walls
 */

// @lc code=start
/**
 * @lc app=leetcode id=2742 lang=csharp
 *
 * [2742] Painting the Walls
 */

using System;
using System.Collections.Generic;

public class Solution {
    public int PaintWalls(int[] cost, int[] time) {
        int n = cost.Length;
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            dp[i] = 500000001;
        }

        for (int i = 0; i < n; i++) {
            for (int j = n; j > 0; j--) {
                dp[j] = Math.Min(dp[j], dp[Math.Max(0, j - time[i] - 1)] + cost[i]);
            }
        }

        return dp[n];
    }
}

// @lc code=end

