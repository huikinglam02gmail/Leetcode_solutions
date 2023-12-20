/*
 * @lc app=leetcode id=2706 lang=csharp
 *
 * [2706] Buy Two Chocolates
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int BuyChoco(int[] prices, int money) {
        Array.Sort(prices);
        if (prices[0] + prices[1] <= money) {
            return money - prices[0] - prices[1];
        } else {
            return money;
        }
    }
}

// @lc code=end

