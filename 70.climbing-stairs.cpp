/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
#include <vector>

class Solution {
public:
    // To reach n, u first need to reach n - 1 or n - 2
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        } else {
            std::vector<int> dp(n, 0);
            dp[0] = 1;
            dp[1] = 2;
            for (int i = 2; i < n; ++i) {
                dp[i] += dp[i - 1];
                dp[i] += dp[i - 2];
            }
            return dp.back();
        }
    }
};

// @lc code=end

