/*
 * @lc app=leetcode id=518 lang=cpp
 *
 * [518] Coin Change II
 */

// @lc code=start
#include <iostream>
#include <vector>

class Solution {
public:
    int change(int amount, std::vector<int>& coins) {
        std::vector<int> dp(amount + 1, 0);
        dp[0] = 1;
        
        for (int coin : coins) {
            for (int i = coin; i <= amount; ++i) {
                dp[i] += dp[i - coin];
            }
        }
        
        return dp[amount];
    }
};
// @lc code=end

