/*
 * @lc app=leetcode id=1289 lang=csharp
 *
 * [1289] Minimum Falling Path Sum II
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    dp[i][j] = minimum of all falling path which ends at row i and column j
    Then we can just iterate through the rows from top to bottom    
    */
    public int MinFallingPathSum(int[][] grid) {
        int n = grid.Length;
        if (n == 1) {
            return grid[0][0];
        }
        
        List<int[]> dp = new List<int[]>();
        for (int i = 0; i < n; i++) {
            List<int[]> dpNew = new List<int[]>();
            if (i == 0) {
                for (int j = 0; j < n; j++) {
                    dpNew.Add(new int[]{grid[i][j], j});
                }
            } else {
                for (int j = 0; j < n; j++) {
                    if (j != dp[0][1]) {
                        dpNew.Add(new int[]{grid[i][j] + dp[0][0], j});
                    } else {
                        dpNew.Add(new int[]{grid[i][j] + dp[1][0], j});
                    }
                }
            }
            dp = dpNew;
            dp.Sort((x, y) => x[0].CompareTo(y[0]));
        }
        
        return dp[0][0];
    }
}

// @lc code=end

