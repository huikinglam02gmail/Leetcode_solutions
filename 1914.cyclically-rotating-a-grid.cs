/*
 * @lc app=leetcode id=1914 lang=csharp
 *
 * [1914] Cyclically Rotating a Grid
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] RotateGrid(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[][] result = new int[m][];
        bool[][] visited = new bool[m][];
        for (int i = 0; i < m; i++) {
            result[i] = new int[n];
            visited[i] = new bool[n];
        }
        
        List<List<int[]>> rings = new List<List<int[]>>();
        
        for (int row = 0; row < m; row++) 
        {
            if (row < n && !visited[row][row])
            {
                List<int[]> current = new List<int[]>();
                int i = row;
                int j = row;
                current.Add(new int[2] { i, j });
                visited[i][j] = true;
                
                while (j + 1 < n && !visited[i][j + 1]) {
                    j++;
                    current.Add(new int[2] { i, j });
                    visited[i][j] = true;
                }
                
                while (i + 1 < m && !visited[i + 1][j]) {
                    i++;
                    current.Add(new int[2] { i, j });
                    visited[i][j] = true;
                }
                
                while (j - 1 >= 0 && !visited[i][j - 1]) {
                    j--;
                    current.Add(new int[2] { i, j });
                    visited[i][j] = true;
                }
                
                while (i - 1 >= 0 && !visited[i - 1][j]) {
                    i--;
                    current.Add(new int[2] { i, j });
                    visited[i][j] = true;
                }
                rings.Add(current);
            }
        }
        
        for (int i = 0; i < rings.Count; i++) {
            for (int j = 0; j < rings[i].Count; j++) {
                int[] current = rings[i][j];
                int[] next = rings[i][(j + k) % (rings[i].Count)];
                result[current[0]][current[1]] = grid[next[0]][next[1]];
            }
        }
        
        return result;
    }
}

// @lc code=end

