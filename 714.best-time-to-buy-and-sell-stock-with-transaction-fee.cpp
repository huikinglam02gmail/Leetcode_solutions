/*
 * @lc app=leetcode id=714 lang=cpp
 *
 * [714] Best Time to Buy and Sell Stock with Transaction Fee
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::max;
using std::max_element;
using std::move;
using std::vector;
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        vector<int> dp {0, 0, 0, 0};
        vector<int> dpNew;
        int n = prices.size();
        
        for (int i = 0; i < n; i++) {
            dpNew = {0, 0, 0, 0};
            
            if (i == 0) {
                dpNew[0] = -prices[i];
            }
            else if (i == 1) {
                dpNew[0] = dp[1] - prices[i];
                dpNew[2] = dp[0] + prices[i] - fee;
                dpNew[3] = dp[0];
            }
            else {
                dpNew[0] = max(dp[1], dp[2]) - prices[i];
                dpNew[1] = max(dp[1], dp[2]);
                dpNew[2] = max(dp[0], dp[3]) + prices[i] - fee;
                dpNew[3] = max(dp[0], dp[3]);
            }

            dp = move(dpNew);
        }
        
        return *max_element(dp.begin(), dp.end());
    }
};
// @lc code=end

