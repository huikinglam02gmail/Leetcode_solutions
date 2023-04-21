/*
 * @lc app=leetcode id=879 lang=csharp
 *
 * [879] Profitable Schemes
 */

// @lc code=start
using System.Linq;
using System;
public class Solution 
{
    long MOD = 1000000007;
    public int ProfitableSchemes(int n, int minProfit, int[] group, int[] profit) 
    {
        long[][] dp = new long[minProfit + 1][];
        dp = dp.Select(x => Enumerable.Repeat(0L, n + 1).ToArray()).ToArray();
        dp[0][0] = 1;
        for (int k = 0; k < group.Length; k++)
        {
            for (int i = minProfit; i >= 0; i--)
            {
                for (int j = n - group[k]; j >= 0; j--)
                {
                    dp[Math.Min(minProfit, i + profit[k])][j + group[k]] += dp[i][j];
                    dp[Math.Min(minProfit, i + profit[k])][j + group[k]] %= MOD;
                }
            }
        }
        return Convert.ToInt32(dp[minProfit].Sum() % MOD);
    }
}
// @lc code=end

