/*
 * @lc app=leetcode id=63 lang=csharp
 *
 * [63] Unique Paths II
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.Length;
        int n = obstacleGrid[0].Length;
        int[][] dp = new int[m][];

        for (int i = 0; i < m; i++) {
            dp[i] = new int[n];
            for (int j = 0; j < n; j++) {
                dp[i][j] = 0;
            }
        }

        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        dp[0][0] = 1;

        int x = 0;
        while (x < m - 1 && obstacleGrid[x + 1][0] == 0) {
            x++;
            dp[x][0] = 1;
        }

        int y = 0;
        while (y < n - 1 && obstacleGrid[0][y + 1] == 0) {
            y++;
            dp[0][y] = 1;
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
}

// @lc code=end

