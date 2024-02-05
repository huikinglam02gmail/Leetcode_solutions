/*
 * @lc app=leetcode id=2806 lang=csharp
 *
 * [2806] Account Balance After Rounded Purchase
 */

// @lc code=start
using System;

public class Solution {
    private int Round(int i) {
        int residual = i / 10;
        return (i % 10 < 5) ? residual * 10 : residual * 10 + 10;
    }

    public int AccountBalanceAfterPurchase(int purchaseAmount) {
        return 100 - Round(purchaseAmount);
    }
}

// @lc code=end

