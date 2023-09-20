/*
 * @lc app=leetcode id=1901 lang=csharp
 *
 * [1901] Find a Peak Element II
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindPeakGrid(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;

        if (m > n) {
            int[] result = FindPeakGrid(Transpose(mat));
            return new int[] { result[1], result[0] };
        } else if (n == 1) {
            return new int[] { 0, 0 };
        } else {
            int left = 0;
            int right = n;

            while (left < right) {
                int mid = left + (right - left) / 2;
                int row = GetMaxRow(mat, mid);

                if ((mid == 0 || mat[row][mid - 1] < mat[row][mid]) &&
                    (mid == n - 1 || mat[row][mid + 1] < mat[row][mid])) {
                    return new int[] { row, mid };
                } else if (mid > 0 && mat[row][mid - 1] > mat[row][mid]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }

            return new int[] { GetMaxRow(mat, left), left };
        }
    }

    private int[][] Transpose(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        int[][] result = new int[n][];

        for (int j = 0; j < n; j++) {
            result[j] = new int[m];
            for (int i = 0; i < m; i++) {
                result[j][i] = mat[i][j];
            }
        }

        return result;
    }

    private int GetMaxRow(int[][] mat, int col) {
        int row = 0;
        int current = -1;

        for (int i = 0; i < mat.Length; i++) {
            if (mat[i][col] > current) {
                current = mat[i][col];
                row = i;
            }
        }

        return row;
    }
}

// @lc code=end

