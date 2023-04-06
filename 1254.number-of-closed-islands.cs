/*
 * @lc app=leetcode id=1254 lang=csharp
 *
 * [1254] Number of Closed Islands
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    int[][] Grid;

    public void contagion(int xStart, int yStart)
    {
        Queue<int[]> queue = new Queue<int[]>();
        queue.Enqueue(new int[2] { xStart, yStart });
        Grid[xStart][yStart] = 1;
        while (queue.TryDequeue(out int[] node))
        {
            List<int[]> neigs = new List<int[]>();
            if (node[0] > 0)
            {
                neigs.Add(new int[2]{node[0] - 1, node[1]});                    
            }
            if (node[1] > 0)
            {
                neigs.Add(new int[2]{node[0], node[1] - 1});                    
            }
            if (node[0] < Grid.Length - 1)
            {
                neigs.Add(new int[2]{node[0] + 1, node[1]});                    
            }
            if (node[1] < Grid[0].Length - 1)
            {
                neigs.Add(new int[2]{node[0], node[1] + 1});                    
            }
            foreach (int[] neig in neigs)
            {
                if (Grid[neig[0]][neig[1]] == 0)
                {
                    queue.Enqueue(neig);
                    Grid[neig[0]][neig[1]] = 1;
                }
            }
        }
    }
    public int ClosedIsland(int[][] grid) 
    {
        Grid = grid;
        int m = Grid.Length;
        int n = Grid[0].Length;
        for (int i = 0; i < m; i++)
        {
            if (Grid[i][0] == 0)
            {
                contagion(i, 0);
            }
            if (Grid[i][n - 1] == 0)
            {
                contagion(i, n - 1);
            }
        }

        for (int i = 0; i < n; i++)
        {
            if (Grid[0][i] == 0)
            {
                contagion(0, i);
            }
            if (Grid[m - 1][i] == 0)
            {
                contagion(m - 1, i);
            }
        }

        int result = 0;
        for (int i = 1; i < m - 1; i++)
        {
            for (int j = 1; j < n - 1; j++)
            {
                if (Grid[i][j] == 0)
                {
                    result++;
                    contagion(i, j);
                }
            }
        }
        return result;
    }
}
// @lc code=end

