/*
 * @lc app=leetcode id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        
        for (int i = 0; i < prices.size() - 1; i++) {
            result += max(0, prices[i + 1] - prices[i]);
        }
        
        return result;
    }
};

// @lc code=end

