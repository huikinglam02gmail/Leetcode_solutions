/*
 * @lc app=leetcode id=2706 lang=cpp
 *
 * [2706] Buy Two Chocolates
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        sort(prices.begin(), prices.end());
        if (prices[0] + prices[1] <= money) {
            return money - prices[0] - prices[1];
        } else {
            return money;
        }
    }
};

// @lc code=end

