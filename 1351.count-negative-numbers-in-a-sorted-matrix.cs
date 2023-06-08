/*
 * @lc app=leetcode id=1351 lang=csharp
 *
 * [1351] Count Negative Numbers in a Sorted Matrix
 */

// @lc code=start
using System;

public class Solution
{
    /*
    Walk a pointer from top right corner to bottom.
    */
    public int CountNegatives(int[][] grid)
    {
        int result = 0;
        int m = grid.Length;
        int n = grid[0].Length;
        int x = 0;
        int y = n - 1;
        
        while (x < m && y >= 0)
        {
            if (grid[x][y] >= 0)
            {
                result += n - 1 - y;
                x++;
            }
            else
            {
                y--;
            }
        }
        
        if (y < 0)
        {
            result += (m - x) * n;
        }
        
        return result;
    }
}

// @lc code=end

