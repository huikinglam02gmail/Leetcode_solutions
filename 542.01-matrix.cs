/*
 * @lc app=leetcode id=542 lang=csharp
 *
 * [542] 01 Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] UpdateMatrix(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        int steps = 0;
        Queue<(int, int)> queue = new Queue<(int, int)>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    queue.Enqueue((i, j));
                }
            }
        }

        int[][] result = new int[m][];
        for (int i = 0; i < m; i++) {
            result[i] = new int[n];
        }

        int[][] directions = new int[][] {
            new int[] { 1, 0 },
            new int[] { -1, 0 },
            new int[] { 0, 1 },
            new int[] { 0, -1 }
        };

        while (queue.Count > 0) {
            int count = queue.Count;
            for (int i = 0; i < count; i++) {
                (int x, int y) = queue.Dequeue();
                result[x][y] = steps;

                foreach (var direction in directions) {
                    int nx = x + direction[0];
                    int ny = y + direction[1];

                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && mat[nx][ny] == 1) {
                        mat[nx][ny] = 0;
                        queue.Enqueue((nx, ny));
                    }
                }
            }
            steps++;
        }

        return result;
    }
}

// @lc code=end

