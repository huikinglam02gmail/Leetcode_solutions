/*
 * @lc app=leetcode id=1738 lang=csharp
 *
 * [1738] Find Kth Largest XOR Coordinate Value
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution 
{
    public int KthLargestValue(int[][] matrix, int k) 
    {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[][] prefixXOR = new int[m][];
        
        for (int i = 0; i < m; i++) 
        {
            prefixXOR[i] = new int[n];
            for (int j = 0; j < n; j++) 
            {
                prefixXOR[i][j] = matrix[i][j];
            }
        }
        
        List<int> allNumbers = new List<int>();
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                if (i > 0) 
                {
                    prefixXOR[i][j] ^= prefixXOR[i - 1][j];
                }
                if (j > 0) 
                {
                    prefixXOR[i][j] ^= prefixXOR[i][j - 1];
                }
                if (i > 0 && j > 0) 
                {
                    prefixXOR[i][j] ^= prefixXOR[i - 1][j - 1];
                }
                allNumbers.Add(prefixXOR[i][j]);
            }
        }
        
        allNumbers.Sort((a, b) => b.CompareTo(a));
        return allNumbers[k - 1];
    }
}

// @lc code=end

