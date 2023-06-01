/*
 * @lc app=leetcode id=1091 lang=csharp
 *
 * [1091] Shortest Path in Binary Matrix
 */

// @lc code=start
using System.Collections.Generic;

public class Solution
{
    public int ShortestPathBinaryMatrix(int[][] grid)
    {
        if (grid[0][0] == 1)
            return -1;

        int m = grid.Length;
        int n = grid[0].Length;
        Queue<(int, int)> queue = new Queue<(int, int)>();
        HashSet<(int, int)> visited = new HashSet<(int, int)>();
        int steps = 1;

        queue.Enqueue((0, 0));
        visited.Add((0, 0));

        while (queue.Count > 0)
        {
            int size = queue.Count;

            for (int i = 0; i < size; i++)
            {
                (int x, int y) = queue.Dequeue();

                if (x == m - 1 && y == n - 1)
                    return steps;

                (int, int)[] neighbours = {
                    (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                    (x, y + 1), (x, y - 1), (x + 1, y - 1),
                    (x + 1, y), (x + 1, y + 1)
                };

                foreach ((int nx, int ny) in neighbours)
                {
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                        !visited.Contains((nx, ny)) && grid[nx][ny] == 0)
                    {
                        queue.Enqueue((nx, ny));
                        visited.Add((nx, ny));
                    }
                }
            }

            steps++;
        }

        return -1;
    }
}

// @lc code=end

