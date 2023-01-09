/*
 * @lc app=leetcode id=1605 lang=csharp
 *
 * [1605] Find Valid Matrix Given Row and Column Sums
 */

// @lc code=start
public class Solution 
{
    public int[][] RestoreMatrix(int[] rowSum, int[] colSum) 
    {
        int m = rowSum.Length;
        int n = colSum.Length;
        int[][] result = new int[m][];
        for (int i = 0; i < m; i++)
        {
            result[i] = new int[n];
            for (int j = 0; j < n; j++)
            {
                result[i][j] = Math.Min(rowSum[i], colSum[j]);
                rowSum[i] -= result[i][j];
                colSum[j] -= result[i][j];
            }
        }
        return result;
    }
}
// @lc code=end

