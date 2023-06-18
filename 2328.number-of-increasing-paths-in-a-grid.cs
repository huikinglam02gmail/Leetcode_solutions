/*
 * @lc app=leetcode id=2328 lang=csharp
 *
 * [2328] Number of Increasing Paths in a Grid
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private int[][] grid;
    private long MOD;
    private Dictionary<Tuple<int, int>, int> memo;
    
    public int CountPaths(int[][] grid) {
        this.grid = grid;
        this.memo = new Dictionary<Tuple<int,int>, int>();
        MOD = 1000000007;
        long result = 0;
        int m = grid.Length;
        int n = grid[0].Length;
        
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                result += DFS(i, j);
                result %= MOD;
            }
        }
        
        return Convert.ToInt32(result);
    }
    
    private int DFS(int row, int col) 
    {
        Tuple<int, int> t = new Tuple<int, int>(row, col);
        if (!memo.ContainsKey(t))
        {
            long result = 1;
            
            if (row + 1 < grid.Length && grid[row + 1][col] > grid[row][col]) {
                result += DFS(row + 1, col);
                result %= MOD;
            }
            
            if (col + 1 < grid[0].Length && grid[row][col + 1] > grid[row][col]) {
                result += DFS(row, col + 1);
                result %= MOD;
            }
            
            if (row > 0 && grid[row - 1][col] > grid[row][col]) {
                result += DFS(row - 1, col);
                result %= MOD;
            }
            
            if (col > 0 && grid[row][col - 1] > grid[row][col]) {
                result += DFS(row, col - 1);
                result %= MOD;
            }

            memo.Add(t, Convert.ToInt32(result));          
        }
        return memo[t];

    }
}

// @lc code=end

