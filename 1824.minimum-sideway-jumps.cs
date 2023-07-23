/*
 * @lc app=leetcode id=1824 lang=csharp
 *
 * [1824] Minimum Sideway Jumps
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    Number of states are limited at each position
    dp[i][j] = number of side jumps needed to reach at (i, j)
    dp[i][j] = Math.Min(dp[i - 1][j], 1 + dp[i][k != j]) if obstable[i] != k
    We aim to get min(dp[n][:]) 
    */
    public int MinSideJumps(int[] obstacles)
    {
        int n = obstacles.Length;
        int[] dp1 = { 1, 0, 1 };
        int[] dp2 = new int[3];
        int[] dp3 = new int[3];
        for (int i = 0; i < n; i++)
        {
            dp1.CopyTo(dp2, 0);
            if (obstacles[i] > 0)
            {
                dp2[obstacles[i] - 1] = 1000000;
            }
            dp2.CopyTo(dp3, 0);
            
            for (int j = 0; j < 2; j++)
            {
                for (int k = j + 1; k < 3; k++)
                {
                    if (obstacles[i] - 1 != j)
                    {
                        dp3[j] = Math.Min(dp3[j], 1 + dp2[k]);
                    }
                    if (obstacles[i] - 1 != k)
                    {
                        dp3[k] = Math.Min(dp3[k], 1 + dp2[j]);
                    }
                }
            }
            
            dp3.CopyTo(dp1, 0);
        }
        
        return dp1.Min();
    }
}

// @lc code=end

