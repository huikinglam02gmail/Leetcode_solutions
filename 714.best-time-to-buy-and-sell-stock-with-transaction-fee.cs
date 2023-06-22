/*
 * @lc app=leetcode id=714 lang=csharp
 *
 * [714] Best Time to Buy and Sell Stock with Transaction Fee
 */

// @lc code=start
using System;

public class Solution {
    public int MaxProfit(int[] prices, int fee) {
        int[] dp = new int[4];
        int n = prices.Length;
        
        for (int i = 0; i < n; i++) {
            int[] dpNew = new int[4];
            
            if (i == 0) {
                dpNew[0] = -prices[i];
            }
            else if (i == 1) {
                dpNew[0] = dp[1] - prices[i];
                dpNew[2] = dp[0] + prices[i] - fee;
                dpNew[3] = dp[0];
            }
            else {
                dpNew[0] = Math.Max(dp[1], dp[2]) - prices[i];
                dpNew[1] = Math.Max(dp[1], dp[2]);
                dpNew[2] = Math.Max(dp[0], dp[3]) + prices[i] - fee;
                dpNew[3] = Math.Max(dp[0], dp[3]);
            }
            
            dp = (int[])dpNew.Clone();
        }
        
        return Math.Max(dp[1], Math.Max(dp[2], dp[3]));
    }
}

// @lc code=end

