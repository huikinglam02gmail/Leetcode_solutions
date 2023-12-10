/*
 * @lc app=leetcode id=867 lang=csharp
 *
 * [867] Transpose Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int[][] Transpose(int[][] matrix)
    {
        List<List<int>> transposed = new List<List<int>>();
        for (int i = 0; i < matrix[0].Length; i++)
        {
            List<int> row = new List<int>();
            for (int j = 0; j < matrix.Length; j++)
            {
                row.Add(matrix[j][i]);
            }
            transposed.Add(row);
        }

        // Convert List<List<int>> to int[][]
        int[][] result = new int[transposed.Count][];
        for (int i = 0; i < transposed.Count; i++)
        {
            result[i] = transposed[i].ToArray();
        }

        return result;
    }
}

// @lc code=end

