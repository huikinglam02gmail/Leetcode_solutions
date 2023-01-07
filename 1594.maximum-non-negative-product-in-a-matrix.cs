/*
 * @lc app=leetcode id=1594 lang=csharp
 *
 * [1594] Maximum Non Negative Product in a Matrix
 */

// @lc code=start
public class Solution 
{
    public int MaxProductPath(int[][] grid) 
    {
        int m = grid.Length;
        int n = grid[0].Length;
        long[][] dpMax = new long[m][];
        long[][] dpMin = new long[m][];
        long MOD = 1000000007;

        for (int i = 0; i < m; i++)
        {
            dpMax[i] = new long[n];
            dpMin[i] = new long[n];
            Array.Fill(dpMax[i], Int64.MinValue);
            Array.Fill(dpMin[i], Int64.MaxValue);
            for (int j = 0; j < n; j++)
            {
                if (i == 0 && j == 0)
                {
                    dpMax[i][j] = grid[i][j];
                    dpMin[i][j] = grid[i][j];
                }
                if (i > 0)
                {
                    if (grid[i][j] >= 0)
                    {
                        dpMax[i][j] = Math.Max(dpMax[i][j], dpMax[i-1][j]*grid[i][j]);
                        dpMin[i][j] = Math.Min(dpMin[i][j], dpMin[i-1][j]*grid[i][j]);                      
                    }
                    if (grid[i][j] <= 0)
                    {
                        dpMax[i][j] = Math.Max(dpMax[i][j], dpMin[i-1][j]*grid[i][j]);
                        dpMin[i][j] = Math.Min(dpMin[i][j], dpMax[i-1][j]*grid[i][j]);                      
                    }
                }
                if (j > 0)
                {
                    if (grid[i][j] >= 0)
                    {
                        dpMax[i][j] = Math.Max(dpMax[i][j], dpMax[i][j - 1]*grid[i][j]);
                        dpMin[i][j] = Math.Min(dpMin[i][j], dpMin[i][j - 1]*grid[i][j]);                      
                    }
                    if (grid[i][j] <= 0)
                    {
                        dpMax[i][j] = Math.Max(dpMax[i][j], dpMin[i][j - 1]*grid[i][j]);
                        dpMin[i][j] = Math.Min(dpMin[i][j], dpMax[i][j - 1]*grid[i][j]);                      
                    }
                }
            }
        }
        Console.WriteLine($"{dpMax[m-1][n-1]}");
        if (dpMax[m-1][n-1] < 0)
        {
            return -1;
        }
        else
        {
            return Convert.ToInt32(dpMax[m-1][n-1] % MOD);
        }
    }
}
// @lc code=end
