/*
 * @lc app=leetcode id=1691 lang=csharp
 *
 * [1691] Maximum Height by Stacking Cuboids 
 */

// @lc code=start
using System.Linq;
using System.Collections.Generic;
using System;
public class Solution 
{
    public int MaxHeight(int[][] cuboids) 
    {
        cuboids = cuboids.Select(x => x.OrderBy(y => - y).ToArray()).OrderBy(x => - x[0]).ThenBy(x => - x[1]).ThenBy(x => - x[2]).ToArray();
        int n = cuboids.Length;
        int[] dp = cuboids.Select(x => x[0]).ToArray();

        int result = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (cuboids[j][0] >= cuboids[i][0] && cuboids[j][1] >= cuboids[i][1] && cuboids[j][2] >= cuboids[i][2])
                {
                    dp[i] = Math.Max(dp[i], cuboids[i][0] + dp[j]);
                }
            }
            result = Math.Max(result, dp[i]);
        }
        return result;
    }
}
// @lc code=end

