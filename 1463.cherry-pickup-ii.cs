/*
 * @lc app=leetcode id=1463 lang=csharp
 *
 * [1463] Cherry Pickup II
 */

// @lc code=start
public class Solution
{
    public int CherryPickup(int[][] grid) 
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int result;
        int choices;
        int[][] dp = new int[n][];
        int[][] dpNew = new int[n][];
        for (int i = 0; i < n; i++)
        {
            dp[i] = new int[n];
            Array.Fill(dp[i], -1);
        }
        dp[0][n-1] = grid[0][0] + grid[0][n-1];
        result = dp[0][n-1];
        for (int i = 1; i < m; i++)
        {
            dpNew = new int[n][];
            for (int j = 0; j < n; j++)
            {
                dpNew[j] = new int[n];
                Array.Fill(dpNew[j], -1);
            }
            for (int j = 0; j < n; j++)
            {
                for (int k = 0; k < n; k++)
                {
                    choices = -1;
                    if (dp[j][k] >= 0)
                    {
                        choices = Math.Max(choices, dp[j][k]);
                    }
                    if (j > 0 && dp[j-1][k] >= 0)
                    {
                        choices = Math.Max(choices, dp[j-1][k]);
                    }
                    if (j < n - 1 && dp[j+1][k] >= 0)
                    {
                        choices = Math.Max(choices, dp[j+1][k]);
                    }
                    if (k > 0 && dp[j][k-1] >= 0)
                    {
                        choices = Math.Max(choices, dp[j][k-1]);
                    }
                    if (k < n - 1 && dp[j][k+1] >= 0)
                    {
                        choices = Math.Max(choices, dp[j][k+1]);
                    }
                    if (j > 0 && k > 0 && dp[j-1][k-1] >= 0)
                    {
                        choices = Math.Max(choices, dp[j-1][k-1]);
                    }
                    if (j < n - 1 && k > 0 && dp[j+1][k-1] >= 0)
                    {
                        choices = Math.Max(choices, dp[j+1][k-1]);
                    }
                    if (j > 0 && k < n - 1 && dp[j-1][k+1] >= 0)
                    {
                        choices = Math.Max(choices, dp[j-1][k+1]);
                    }
                    if (j < n - 1 && k < n - 1 && dp[j+1][k+1] >= 0)
                    {
                        choices = Math.Max(choices, dp[j+1][k+1]);
                    }
                    if (choices >= 0)
                    {
                        if (j != k)
                        {
                            dpNew[j][k] = grid[i][j] + grid[i][k];
                        }
                        else
                        {
                            dpNew[j][k] = grid[i][j];
                        }
                        dpNew[j][k] += choices;
                        result = Math.Max(result, dpNew[j][k]);
                    }
                }
            }
            dp = dpNew;
        }
        return result;
    }
}
// @lc code=end

