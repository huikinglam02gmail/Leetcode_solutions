/*
 * @lc app=leetcode id=122 lang=csharp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
using System;

public class Solution {
    public int MaxProfit(int[] prices) {
        int result = 0;
        
        for (int i = 0; i < prices.Length - 1; i++) {
            result += Math.Max(0, prices[i + 1] - prices[i]);
        }
        
        return result;
    }
}

// @lc code=end

