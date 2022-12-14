/*
 * @lc app=leetcode id=931 lang=csharp
 *
 * [931] Minimum Falling Path Sum
 */

// @lc code=start
public class Solution 
{
    public int MinFallingPathSum(int[][] matrix) 
    {
        int n = matrix.Length;
        List<int> dp = new List<int>();
        for (int j = 0; j < n; j++)
        {
            dp.Add(matrix[0][j]);
        }
        for (int i = 1; i < n; i++)
        {
            List<int> dpNew = matrix[i].Select(x => x).ToList();
            for (int j = 0; j < n; j++)
            {
                int toAdd = dp[j];
                if (j > 0)
                {
                    toAdd = Math.Min(toAdd, dp[j-1]);
                }
                if (j < n - 1)
                {
                    toAdd = Math.Min(toAdd, dp[j+1]);
                }
                dpNew[j] += toAdd;
            }
            dp = dpNew.Select(x => x).ToList();
        }
        return dp.Min(x => x);
    }
}
// @lc code=end

