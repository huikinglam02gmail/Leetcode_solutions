/*
 * @lc app=leetcode id=1219 lang=csharp
 *
 * [1219] Path with Maximum Gold
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private int[][] grid;
    
    public int Dfs(int x, int y) {
        if (x < 0 || y < 0 || x >= grid.Length || y >= grid[0].Length || grid[x][y] == 0) return 0;
        int original = grid[x][y];
        int result = 0;
        int[][] neigs = { new int[] { x - 1, y }, new int[] { x + 1, y }, new int[] { x, y - 1 }, new int[] { x, y + 1 } };
        grid[x][y] = 0;
        foreach (var nei in neigs) {
            result = Math.Max(result, Dfs(nei[0], nei[1]));
        }
        grid[x][y] = original;
        return result + original;
    }
    
    public int GetMaximumGold(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int total = 0;
        foreach (var row in grid) {
            foreach (var cell in row) {
                total += cell;
            }
        }
        this.grid = grid;
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result = Math.Max(result, Dfs(i, j));
                if (result == total) return total;
            }
        }
        return result;
    }
}

// @lc code=end

