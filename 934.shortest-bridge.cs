/*
 * @lc app=leetcode id=934 lang=csharp
 *
 * [934] Shortest Bridge
 */

// @lc code=start
using System.Collections.Generic;

public class Solution
{
    public int ShortestBridge(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int count = 2;
        int[][] neigs = new int[][] { new int[] { 0, 1 }, new int[] { 0, -1 }, new int[] { 1, 0 }, new int[] { -1, 0 } };
        Queue<int[]> dq = new Queue<int[]>();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 1)
                {
                    dq.Clear();
                    dq.Enqueue(new int[] { i, j });
                    grid[i][j] = count;

                    while (dq.TryDequeue(out int[] node))
                    {
                        foreach (int[] neig in neigs)
                        {
                            int[] nxt = new int[] { node[0] + neig[0], node[1] + neig[1] };
                            if (nxt[0] >= 0 && nxt[0] < m && nxt[1] >= 0 && nxt[1] < n && grid[nxt[0]][nxt[1]] == 1)
                            {
                                dq.Enqueue(nxt);
                                grid[nxt[0]][nxt[1]] = count;
                            }
                        }
                    }

                    count++;
                }
            }
        }

        int steps = 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 3)
                {
                    dq.Enqueue(new int[] { i, j });
                }
            }
        }

        while (dq.Count > 0)
        {
            int size = dq.Count;

            for (int i = 0; i < size; i++)
            {
                int[] node = dq.Dequeue();

                foreach (int[] neig in neigs)
                {
                    int[] nxt = new int[] { node[0] + neig[0], node[1] + neig[1] };

                    if (nxt[0] >= 0 && nxt[0] < m && nxt[1] >= 0 && nxt[1] < n && grid[nxt[0]][nxt[1]] != 3)
                    {
                        if (grid[nxt[0]][nxt[1]] == 2)
                        {
                            return steps;
                        }

                        dq.Enqueue(nxt);
                        grid[nxt[0]][nxt[1]] = 3;
                    }
                }
            }

            steps++;
        }

        return -1; // Return -1 if no bridge is found
    }
}

// @lc code=end

