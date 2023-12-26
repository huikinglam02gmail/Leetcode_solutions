/*
 * @lc app=leetcode id=1155 lang=cpp
 *
 * [1155] Number of Dice Rolls With Target Sum
 */

// @lc code=start
#include <vector>
#include <cmath>

class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        const int MOD = pow(10, 9) + 7;
        std::vector<std::vector<int>> dp(n, std::vector<int>(target + 1, 0));

        for (int j = 1; j <= std::min(k, target); j++) {
            dp[0][j] += 1;
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j <= target; j++) {
                for (int l = 1; l <= k; l++) {
                    if (j + l < target + 1) {
                        dp[i + 1][j + l] = (dp[i + 1][j + l] + dp[i][j]) % MOD;
                    }
                }
            }
        }

        return dp[n - 1][target];
    }
};

// @lc code=end

