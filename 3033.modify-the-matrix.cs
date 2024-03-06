/*
 * @lc app=leetcode id=3033 lang=csharp
 *
 * [3033] Modify the Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] ModifiedMatrix(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        for (int j = 0; j < n; j++) {
            int maxEle = -1;
            List<int> negOnes = new List<int>();
            for (int i = 0; i < m; i++) {
                maxEle = Math.Max(maxEle, matrix[i][j]);
                if (matrix[i][j] == -1) negOnes.Add(i);
            }
            foreach (int i in negOnes) matrix[i][j] = maxEle;
        }
        return matrix;
    }
}

// @lc code=end

