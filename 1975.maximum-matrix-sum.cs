/*
 * @lc app=leetcode id=1975 lang=csharp
 *
 * [1975] Maximum Matrix Sum
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxMatrixSum(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int zeros = 0, negs = 0;
        long S = 0, minAbsSoFar = long.MaxValue;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                S += Math.Abs(matrix[i][j]);
                if (matrix[i][j] == 0) {
                    zeros++;
                }
                else if (matrix[i][j] < 0) {
                    negs++;
                }
                minAbsSoFar = Math.Min(minAbsSoFar, Math.Abs(matrix[i][j]));
            }
        }

        return zeros > 0 || negs % 2 == 0 ? S : S - 2 * minAbsSoFar;
    }
}

// @lc code=end

