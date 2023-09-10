/*
 * @lc app=leetcode id=1359 lang=cpp
 *
 * [1359] Count All Valid Pickup and Delivery Options
 */

// @lc code=start
class Solution {
public:
    int countOrders(int n) {
        long long result = 1;
        long long MOD = 1000000007;

        for (int i = 2; i <= n; i++) {
            result *= i;
            result %= MOD;
            result *= 2 * i - 1;
            result %= MOD;
        }

        return static_cast<int>(result);
    }
};

// @lc code=end

