/*
 * @lc app=leetcode id=2218 lang=csharp
 *
 * [2218] Maximum Value of K Coins From Piles
 */

// @lc code=start
using System.Linq;
using System.Collections.Generic;
using System;
public class Solution 
{
    public int MaxValueOfCoins(IList<IList<int>> piles, int k) 
    {
        int n = piles.Count;
        int[][] dp = new int[n + 1][];
        dp = dp.Select(x => Enumerable.Repeat(0, k + 1).ToArray()).ToArray();
        int prefixSum;
        for (int i = 0; i < n; i++)
        {
            prefixSum = 0;
            for (int j = 0; j < piles[i].Count + 1; j++)
            {
                for (int l = 0; l <= k - j; l++)
                {
                    dp[i + 1][l + j] = Math.Max(dp[i + 1][l + j], dp[i][l] + prefixSum);
                }
                if (j < piles[i].Count)
                {
                    prefixSum += piles[i][j];
                }
            }
        }
        return dp[n][k];
    }
}
// @lc code=end

