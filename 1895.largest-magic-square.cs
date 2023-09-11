/*
 * @lc app=leetcode id=1895 lang=csharp
 *
 * [1895] Largest Magic Square
 */

// @lc code=start
public class Solution {
    public int LargestMagicSquare(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        int[][] rowSum = new int[m][];
        for (int i = 0; i < m; i++) {
            rowSum[i] = new int[n + 1];
        }

        int[][] colSum = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            colSum[i] = new int[n];
        }

        int[][] leftDiagonalSum = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            leftDiagonalSum[i] = new int[n + 1];
        }

        int[][] rightDiagonalSum = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            rightDiagonalSum[i] = new int[n + 1];
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j];
                colSum[i + 1][j] = colSum[i][j] + grid[i][j];
                leftDiagonalSum[i + 1][j] = leftDiagonalSum[i][j + 1] + grid[i][j];
                rightDiagonalSum[i + 1][j + 1] = rightDiagonalSum[i][j] + grid[i][j];
            }
        }

        for (int k = Math.Min(m, n); k > 0; k--) {
            for (int i = m - 1; i >= k - 1; i--) {
                for (int j = n - 1; j >= k - 1; j--) {
                    int S = rightDiagonalSum[i + 1][j + 1] - rightDiagonalSum[i + 1 - k][j + 1 - k];
                    bool allS = true;
                    allS = allS && (leftDiagonalSum[i + 1][j + 1 - k] - leftDiagonalSum[i + 1 - k][j + 1] == S);
                    for (int l = i - k + 1; l <= i; l++) {
                        allS = allS && (rowSum[l][j + 1] - rowSum[l][j + 1 - k] == S);
                    }
                    for (int l = j - k + 1; l <= j; l++) {
                        allS = allS && (colSum[i + 1][l] - colSum[i + 1 - k][l] == S);
                    }
                    if (allS) {
                        return k;
                    }
                }
            }
        }
        return -1;
    }
}

// @lc code=end

