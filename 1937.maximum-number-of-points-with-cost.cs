/*
 * @lc app=leetcode id=1937 lang=csharp
 *
 * [1937] Maximum Number of Points with Cost
 */

// @lc code=start
using System;

public class Solution {
    public long MaxPoints(int[][] points) {
        int m = points.Length;
        int n = points[0].Length;
        long[] dp = points[0].Select(x => (long)x).ToArray();

        for (int i = 0; i < m - 1; i++) 
        {
            long[] dpNew = points[i + 1].Select(x => (long)x).ToArray();
            for (int j = n - 2; j >= 0; j--) 
            {
                dp[j] = Math.Max(dp[j], dp[j + 1] - 1);
            }

            for (int j = 0; j < n; j++) 
            {
                if (j > 0) 
                {
                    dp[j] = Math.Max(dp[j], dp[j - 1] - 1);
                }

                dpNew[j] += dp[j];
            }
            dp = dpNew;
        }

        return dp.Max();
    }
}

// @lc code=end

