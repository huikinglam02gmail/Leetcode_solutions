/*
 * @lc app=leetcode id=1878 lang=csharp
 *
 * [1878] Get Biggest Three Rhombus Sums in a Grid
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] GetBiggestThree(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        HashSet<int> result = new HashSet<int>();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int maxSize = (m - 1 - i) / 2;
                int trueMaxSize = 0;
                int j1 = j, j2 = j;
                while (trueMaxSize <= maxSize && j1 < n && j2 >= 0) {
                    trueMaxSize++;
                    j1++;
                    j2--;
                }
                for (int k = 0; k < trueMaxSize; k++) {
                    int x = i, y = j;
                    int current = 0;
                    for (int l = 0; l < k; l++) {
                        x++;
                        y++;
                        current += grid[x][y];
                    }
                    for (int l = 0; l < k; l++) {
                        x++;
                        y--;
                        current += grid[x][y];
                    }
                    for (int l = 0; l < k; l++) {
                        x--;
                        y--;
                        current += grid[x][y];
                    }
                    for (int l = 0; l < k; l++) {
                        x--;
                        y++;
                        current += grid[x][y];
                    }
                    if (k > 0) {
                        result.Add(current);
                    } else {
                        result.Add(grid[x][y]);
                    }
                }
            }
        }
        
        int[] sortedResult = result.OrderByDescending(x => x).ToArray();
        return sortedResult.Take(3).ToArray();
    }
}

// @lc code=end

