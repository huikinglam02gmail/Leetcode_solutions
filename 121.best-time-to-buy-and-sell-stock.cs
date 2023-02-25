/*
 * @lc app=leetcode id=121 lang=csharp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
using System;
public class Solution 
{
    public int MaxProfit(int[] prices) 
    {
        int profit = 0;
        int minSoFar = 10001;

        foreach (int price in prices)
        {
            profit = Math.Max(profit, price - minSoFar);
            minSoFar = Math.Min(minSoFar, price);
        }    
        return profit;
    }
}
// @lc code=end

