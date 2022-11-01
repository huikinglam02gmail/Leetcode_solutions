/*
 * @lc app=leetcode id=1706 lang=csharp
 *
 * [1706] Where Will the Ball Fall
 */

// @lc code=start
public class Solution {
    int[][] matrix;
    int m;
    int n;
    public int dfs(int j, int i)
    {
        if (i == m)
        {
            return j;
        }
        if (matrix[i][j] == 1)
        {
            if (j < n-1 && matrix[i][j+1]==1)
            {
                return dfs(j+1,i+1);
            }
            else
            {
                return -1;
            }
        }
        else
        {
            if (j > 0 && matrix[i][j-1]==-1)
            {
                return dfs(j-1,i+1);
            }
            else
            {
                return -1;
            }
        }
    }
    public int[] FindBall(int[][] grid) {
        matrix = grid;
        m = grid.Length;
        n = grid[0].Length;
        int[] result = new int[n];
        for (int j = 0; j < n; j++)
        {
            result[j] = dfs(j,0);
        }
        return result;
    }
}
// @lc code=end

