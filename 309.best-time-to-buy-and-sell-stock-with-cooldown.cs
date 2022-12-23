/*
 * @lc app=leetcode id=309 lang=csharp
 *
 * [309] Best Time to Buy and Sell Stock with Cooldown
 */

// @lc code=start
public class Solution 
{
    public int MaxProfit(int[] prices) 
    {
        int n = prices.Length;
        if (n == 1)
        {
            return 0;
        }    
        else if (n == 2)
        {
            return Math.Max(0, prices[1] - prices[0]);
        }
        else
        {
            int[] dp = new int[4];
            int[] dpNew = new int[4];
            Array.Fill(dp, 0);
            for (int i = 0; i < n; i++)
            {
                Array.Fill(dpNew, 0);
                if (i == 0)
                {
                    dpNew[0] -= prices[i];
                }
                else if (i == 1)
                {
                    dpNew[0] = dp[1] - prices[i];
                    dpNew[2] = prices[i] + dp[0];
                    dpNew[3] = dp[0];
                }
                else
                {
                    dpNew[0] = dp[1] - prices[i];
                    dpNew[1] = Math.Max(dp[1], dp[2]);
                    dpNew[2] = prices[i] + Math.Max(dp[0], dp[3]);
                    dpNew[3] = Math.Max(dp[0], dp[3]);
                }
                Array.Copy(dpNew, dp, 4);
            }
            return dp.Max(x => x);
        }
    }
}
// @lc code=end

