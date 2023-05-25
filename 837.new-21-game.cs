/*
 * @lc app=leetcode id=837 lang=csharp
 *
 * [837] New 21 Game
 */

// @lc code=start
using System;
public class Solution 
{
    public double New21Game(int n, int k, int maxPts) 
    {
        double[] dp = new double[n + 1];
        dp[0] = 1;
        double windowSum = 0;

        for (int i = 1; i <= n; i++)
        {
            if (maxPts < i && i < k + 1 + maxPts)
            {
                windowSum -= dp[i - maxPts - 1];
            }
            if (i < k + 1)
            {
                windowSum += dp[i - 1];
            }
            dp[i] += windowSum / maxPts;
        }

        double sumDp = 0;
        for (int i = k; i <= n; i++)
        {
            sumDp += dp[i];
        }

        return sumDp;
    }
}
// @lc code=end

