/*
 * @lc app=leetcode id=2806 lang=cpp
 *
 * [2806] Account Balance After Rounded Purchase
 */

// @lc code=start
class Solution {
public:
    int round(int i) {
        int residual = i / 10;
        return (i % 10 < 5) ? residual * 10 : residual * 10 + 10;
    }

    int accountBalanceAfterPurchase(int purchaseAmount) {
        return 100 - round(purchaseAmount);
    }
};

// @lc code=end

