/*
 * @lc app=leetcode id=766 lang=csharp
 *
 * [766] Toeplitz Matrix
 */

// @lc code=start
public class Solution {
    public bool IsToeplitzMatrix(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (matrix[i][j] != matrix[i-1][j-1])
                {
                    return false;
                }
            }
        }
        return true;
    }
}
// @lc code=end

