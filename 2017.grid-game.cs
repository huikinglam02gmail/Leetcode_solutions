/*
 * @lc app=leetcode id=2017 lang=csharp
 *
 * [2017] Grid Game
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    First robot will proceed to the next row at some column. If it proceeds at index i, the second robot can get max(sum(grid[0][i + 1:]), sum(grid[:i]))
    */
    public long GridGame(int[][] grid)
    {
        long result = long.MaxValue;
        long top = grid[0].Select(x => (long)x).Sum(), bottom = 0;

        for (int i = 0; i < grid[0].Length; i++)
        {
            top -= grid[0][i];
            if (i > 0) bottom += grid[1][i - 1];
            result = Math.Min(result, Math.Max(top, bottom));
        }

        return result;
    }
}

// @lc code=end

