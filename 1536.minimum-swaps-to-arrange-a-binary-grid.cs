/*
 * @lc app=leetcode id=1536 lang=csharp
 *
 * [1536] Minimum Swaps to Arrange a Binary Grid
 */

// @lc code=start
public class Solution 
{
    public int MinSwaps(int[][] grid) 
    {
        int n = grid.Length;
        int[] row = new int[n];
        Array.Fill(row, -1);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 1)
                {
                    row[i] = j;
                }
            }
        }    

        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            int j = i + 1;
            while (row[i] > i && j < n)
            {
                if (row[j] <= i)
                {
                    for (int k = j; k > i; k--)
                    {
                        int temp = row[k];
                        row[k] = row[k-1];
                        row[k-1] = temp;
                        ans++;
                    }
                }
                else
                {
                    j++;
                }
            }
            if (row[i] > i)
            {
                return -1;
            }
        }
        return ans;
    }
}
// @lc code=end

