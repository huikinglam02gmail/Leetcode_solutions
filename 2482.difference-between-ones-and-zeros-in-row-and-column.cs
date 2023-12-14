/*
 * @lc app=leetcode id=2482 lang=csharp
 *
 * [2482] Difference Between Ones and Zeros in Row and Column
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    onesRow[i] = n - zerosRow[i]
    onesCol[j] = m - zerosCol[j]
    diff[i][j] = n - 2 * zerosRow[i] + m - 2 * zerosCol[j]
    */
    public int[][] OnesMinusZeros(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] zerosRow = new int[m];
        int[] zerosCol = new int[n];
        int[][] diff = new int[m][];
        for (int i = 0; i < m; i++) {
            diff[i] = new int[n];
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    zerosRow[i]++;
                    zerosCol[j]++;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                diff[i][j] = m + n - 2 * (zerosRow[i] + zerosCol[j]);
            }
        }

        return diff;
    }
}

// @lc code=end

