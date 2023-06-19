/*
 * @lc app=leetcode id=1765 lang=csharp
 *
 * [1765] Map of Highest Peak
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int[][] HighestPeak(int[][] isWater) {
        int m = isWater.Length;
        int n = isWater[0].Length;
        int[][] height = new int[m][];
        for (int i = 0; i < m; i++) {
            height[i] = new int[n];
        }
        
        Queue<(int, int)> queue = new Queue<(int, int)>();
        HashSet<(int, int)> visited = new HashSet<(int, int)>();
        int current = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j] == 1) {
                    queue.Enqueue((i, j));
                    visited.Add((i, j));
                }
            }
        }
        
        while (queue.Count > 0) {
            int size = queue.Count;
            
            for (int i = 0; i < size; i++) {
                (int x, int y) = queue.Dequeue();
                height[x][y] = current;
                
                int[][] neighbors = {
                    new int[] { x + 1, y },
                    new int[] { x - 1, y },
                    new int[] { x, y + 1 },
                    new int[] { x, y - 1 }
                };
                
                foreach (int[] neighbor in neighbors) {
                    int nx = neighbor[0];
                    int ny = neighbor[1];
                    
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited.Contains((nx, ny))) {
                        visited.Add((nx, ny));
                        queue.Enqueue((nx, ny));
                    }
                }
            }
            
            current++;
        }
        
        return height;
    }
}

// @lc code=end

