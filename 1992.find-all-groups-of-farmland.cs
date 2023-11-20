/*
 * @lc app=leetcode id=1992 lang=csharp
 *
 * [1992] Find All Groups of Farmland
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] FindFarmland(int[][] land) {
        int m = land.Length;
        int n = land[0].Length;
        List<IList<int>> result = new List<IList<int>>();
        bool[,] visited = new bool[m, n];
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                visited[i, j] = (land[i][j] == 0);
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i, j]) {
                    Queue<int[]> queue = new Queue<int[]>();
                    queue.Enqueue(new int[] { i, j, i, j });
                    visited[i, j] = true;

                    while (queue.Count > 0) {
                        int[] coordinates = queue.Dequeue();
                        int x1 = coordinates[0], y1 = coordinates[1], x2 = coordinates[2], y2 = coordinates[3];

                        if ((x2 == m - 1 || land[x2 + 1][y2] == 0) && (y2 == n - 1 || land[x2][y2 + 1] == 0)) {
                            result.Add(new List<int> { x1, y1, x2, y2 });
                        } else {
                            if (x2 + 1 < m && !visited[x2 + 1, y2]) {
                                visited[x2 + 1, y2] = true;
                                queue.Enqueue(new int[] { x1, y1, x2 + 1, y2 });
                            }
                            if (y2 + 1 < n && !visited[x2, y2 + 1]) {
                                visited[x2, y2 + 1] = true;
                                queue.Enqueue(new int[] { x1, y1, x2, y2 + 1 });
                            }
                        }
                    }
                }
            }
        }

        return result.Select(x => x.ToArray()).ToArray();
    }
}

// @lc code=end

