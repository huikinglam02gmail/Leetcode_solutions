/*
 * @lc app=leetcode id=861 lang=csharp
 *
 * [861] Score After Flipping Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Greedy approach
    First column is larger than sum of all on the right
    1000 = 8 > 0111 = 7
    Therefore, one must flip all rows with first column 0s to 1s
    Then for each column, count max(# 1s, # 0s)    
    */
    public int MatrixScore(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                for (int j = 0; j < n; j++) {
                    grid[i][j] = (grid[i][j] == 0) ? 1 : 0;
                }
            }
        }
        int score = 0;
        for (int j = 0; j < n; j++) {
            List<int> col = new List<int>();
            for (int i = 0; i < m; i++) {
                col.Add(grid[i][j]);
            }
            score += (1 << (n - 1 - j)) * Math.Max(col.FindAll(x => x == 1).Count, col.FindAll(x => x == 0).Count);
        }
        return score;
    }
}

// @lc code=end

