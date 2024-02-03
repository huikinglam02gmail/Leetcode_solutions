/*
 * @lc app=leetcode id=1043 lang=csharp
 *
 * [1043] Partition Array for Maximum Sum
 */

// @lc code=start
using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int MaxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.Length;
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            int currMax = 0;
            for (int j = i - 1; j > Math.Max(i - k - 1, -1); j--) {
                currMax = Math.Max(currMax, arr[j]);
                dp[i] = Math.Max(dp[i], dp[j] + (i - j) * currMax);
            }
        }

        return dp[n];
    }
}

// @lc code=end

