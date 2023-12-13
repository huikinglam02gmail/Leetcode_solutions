/*
 * @lc app=leetcode id=1582 lang=csharp
 *
 * [1582] Special Positions in a Binary Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int NumSpecial(int[][] mat) {
        int result = 0;
        int[] rowSum = new int[mat.Length];
        int[] columnSum = new int[mat[0].Length];

        for (int i = 0; i < mat.Length; i++) {
            for (int j = 0; j < mat[0].Length; j++) {
                rowSum[i] += mat[i][j];
                columnSum[j] += mat[i][j];
            }
        }

        for (int i = 0; i < mat.Length; i++) {
            for (int j = 0; j < mat[0].Length; j++) {
                if (mat[i][j] == 1 && rowSum[i] == 1 && columnSum[j] == 1) {
                    result++;
                }
            }
        }

        return result;
    }
}

// @lc code=end

