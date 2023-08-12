/*
 * @lc app=leetcode id=63 lang=cpp
 *
 * [63] Unique Paths II
 */

// @lc code=start
#include <iostream>
#include <vector>

class Solution {
public:
    int uniquePathsWithObstacles(std::vector<std::vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, 0));

        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        dp[0][0] = 1;

        int i = 0;
        while (i < m - 1 && obstacleGrid[i + 1][0] == 0) {
            i++;
            dp[i][0] = 1;
        }

        int j = 0;
        while (j < n - 1 && obstacleGrid[0][j + 1] == 0) {
            j++;
            dp[0][j] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 0) {
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
                }
            }
        }

        return dp[m - 1][n - 1];
    }
};

// @lc code=end

