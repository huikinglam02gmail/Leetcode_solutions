/*
 * @lc app=leetcode id=2639 lang=csharp
 *
 * [2639] Find the Width of Columns of a Grid
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindColumnWidth(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] result = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[j] = Math.Max(result[j], grid[i][j].ToString().Length);
            }
        }

        return result;
    }
}

// @lc code=end

