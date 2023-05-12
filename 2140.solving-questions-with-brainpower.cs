/*
 * @lc app=leetcode id=2140 lang=csharp
 *
 * [2140] Solving Questions With Brainpower
 */

// @lc code=start
using System;
public class Solution 
{
    public long MostPoints(int[][] questions) 
    {
        int n = questions.Length;
        long[] dp = new long[n];
        Array.Fill(dp, 0);
        for (int i = n - 1; i >= 0; i--)
        {
            dp[i] = questions[i][0];
            if (i + 1 + questions[i][1] < n)
            {
                dp[i] += dp[i + 1 + questions[i][1]];
            }
            if (i < n - 1)
            {
                dp[i] = Math.Max(dp[i], dp[i + 1]);
            }                
        }
        return dp[0];
    }
}
// @lc code=end

