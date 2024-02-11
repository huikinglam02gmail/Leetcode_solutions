/*
 * @lc app=leetcode id=1463 lang=cpp
 *
 * [1463] Cherry Pickup II
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int cherryPickup(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, -1));
        dp[0][n - 1] = grid[0][0] + grid[0][n - 1];
        int result = grid[0][0] + grid[0][n - 1];

        for (int i = 1; i < m; ++i) {
            std::vector<std::vector<int>> dpNew(n, std::vector<int>(n, -1));
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < n; ++k) {
                    int choices = -1;
                    if (dp[j][k] >= 0) choices = std::max(choices, dp[j][k]);
                    if (j > 0 && dp[j - 1][k] >= 0) choices = std::max(choices, dp[j - 1][k]);
                    if (j < n - 1 && dp[j + 1][k] >= 0) choices = std::max(choices, dp[j + 1][k]);
                    if (k > 0 && dp[j][k - 1] >= 0) choices = std::max(choices, dp[j][k - 1]);
                    if (k < n - 1 && dp[j][k + 1] >= 0) choices = std::max(choices, dp[j][k + 1]);
                    if (j > 0 && k > 0 && dp[j - 1][k - 1] >= 0) choices = std::max(choices, dp[j - 1][k - 1]);
                    if (j < n - 1 && k > 0 && dp[j + 1][k - 1] >= 0) choices = std::max(choices, dp[j + 1][k - 1]);
                    if (j > 0 && k < n - 1 && dp[j - 1][k + 1] >= 0) choices = std::max(choices, dp[j - 1][k + 1]);
                    if (j < n - 1 && k < n - 1 && dp[j + 1][k + 1] >= 0) choices = std::max(choices, dp[j + 1][k + 1]);
                    if (choices >= 0) {
                        if (j != k) dpNew[j][k] = grid[i][j] + grid[i][k];
                        else dpNew[j][k] = grid[i][j];
                        dpNew[j][k] += choices;
                        result = std::max(result, dpNew[j][k]);
                    }
                }
            }
            dp = dpNew;
        }

        return result;
    }
};

// @lc code=end

