/*
 * @lc app=leetcode id=1074 lang=csharp
 *
 * [1074] Number of Submatrices That Sum to Target
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) {
        int m = matrix.Length;
        int n = matrix[0].Length;

        int[,] prefixSums = new int[m + 1, n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSums[i, j] = matrix[i - 1][j - 1];
                if (j > 1) prefixSums[i, j] += prefixSums[i, j - 1];
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                Dictionary<int, int> cumuSumSeen = new Dictionary<int, int>();
                int cumuSum = 0;

                for (int row = 1; row <= m; row++) {
                    cumuSum += prefixSums[row, j] - prefixSums[row, i];
                    if (cumuSum - target == 0) {
                        result++;
                    }

                    if (cumuSumSeen.ContainsKey(cumuSum - target)) {
                        result += cumuSumSeen[cumuSum - target];
                    }

                    if (cumuSumSeen.ContainsKey(cumuSum)) {
                        cumuSumSeen[cumuSum]++;
                    } else {
                        cumuSumSeen[cumuSum] = 1;
                    }
                }
            }
        }

        return result;
    }
}

// @lc code=end

