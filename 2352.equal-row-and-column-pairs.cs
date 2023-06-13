/*
 * @lc app=leetcode id=2352 lang=csharp
 *
 * [2352] Equal Row and Column Pairs
 */

// @lc code=start
using System.Linq;
using System;
using System.Collections.Generic;
public class Solution 
{
    /*
     * Transpose the grid, then compare row by row   
     */

    public int[][] Transpose(int[][] matrix)
    {
        int[][] transposed = new int[matrix[0].Length][];
        for (int i = 0; i < matrix[0].Length; i++)
        {
            transposed[i] = new int[matrix.Length];
            for (int j = 0; j < matrix.Length; j++)
            {
                transposed[i][j] = matrix[j][i];
            }
        }
        return transposed;
    }

    public int EqualPairs(int[][] grid)
    {
        int[][] transposedGrid = Transpose(grid);
        int result = 0;
        for (int i = 0; i < grid.Length; i++)
        {
            for (int j = 0; j < grid.Length; j++)
            {
                if (Enumerable.SequenceEqual(grid[i], transposedGrid[j]))
                {
                    result++;
                }
            }
        }
        return result;
    }
}
// @lc code=end

