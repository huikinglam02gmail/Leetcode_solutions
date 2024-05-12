/*
 * @lc app=leetcode id=2373 lang=csharp
 *
 * [2373] Largest Local Values in a Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] LargestLocal(int[][] grid) {
        List<int[]> result = new List<int[]>();
        int n = grid.Length;
        for (int i = 1; i < n - 1; i++) {
            int[] row = new int[n - 2];
            for (int j = 1; j < n - 1; j++) {
                row[j - 1] = Math.Max(Math.Max(Math.Max(Math.Max(Math.Max(Math.Max(Math.Max(grid[i - 1][j - 1], grid[i - 1][j]), grid[i - 1][j + 1]), grid[i][j - 1]), grid[i][j]), grid[i][j + 1]), grid[i + 1][j - 1]), Math.Max(grid[i + 1][j], grid[i + 1][j + 1]));
            }
            result.Add(row);
        }
        return result.ToArray();
    }
}

// @lc code=end

