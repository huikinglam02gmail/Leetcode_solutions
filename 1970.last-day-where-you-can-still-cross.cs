/*
 * @lc app=leetcode id=1970 lang=csharp
 *
 * [1970] Last Day Where You Can Still Cross
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    private HashSet<(int, int)> sea;
    private int row;
    private int col;

    private bool CanPass()
    {
        HashSet<(int, int)> visited = new HashSet<(int, int)>();
        for (int j = 0; j < col; j++)
        {
            if (!visited.Contains((0, j)) && !sea.Contains((0, j)))
            {
                Queue<(int, int)> dq = new Queue<(int, int)>();
                dq.Enqueue((0, j));
                visited.Add((0, j));
                while (dq.Count > 0)
                {
                    (int x, int y) = dq.Dequeue();
                    if (x == row - 1)
                    {
                        return true;
                    }
                    int[][] neigs = new int[][]
                    {
                        new int[] { x - 1, y },
                        new int[] { x + 1, y },
                        new int[] { x, y - 1 },
                        new int[] { x, y + 1 }
                    };
                    foreach (int[] neig in neigs)
                    {
                        (int nx, int ny) = (neig[0], neig[1]);
                        if (!visited.Contains((nx, ny)) && !sea.Contains((nx, ny)) && nx >= 0 && nx < row && ny >= 0 && ny < col)
                        {
                            visited.Add((nx, ny));
                            dq.Enqueue((nx, ny));
                        }
                    }
                }
            }
        }
        return false;
    }

    public int LatestDayToCross(int row, int col, int[][] cells)
    {
        sea = new HashSet<(int, int)>();
        this.row = row;
        this.col = col;
        int l = 0;
        int r = row * col;
        while (l < r)
        {
            int mid = l + (r - l) / 2;
            sea = new HashSet<(int, int)>();
            for (int i = 0; i < mid; i++)
            {
                int x = cells[i][0] - 1;
                int y = cells[i][1] - 1;
                sea.Add((x, y));
            }
            if (CanPass())
            {
                l = mid + 1;
            }
            else
            {
                r = mid;
            }
        }
        return l - 1;
    }
}

// @lc code=end

