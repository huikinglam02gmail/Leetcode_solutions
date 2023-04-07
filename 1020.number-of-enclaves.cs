/*
 * @lc app=leetcode id=1020 lang=csharp
 *
 * [1020] Number of Enclaves
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
public class Solution 
{
    int[][] Grid;
    public void bfs(int xStart, int yStart)
    {
        if (Grid[xStart][yStart] == 1)
        {
            Queue<int[]> queue = new Queue<int[]>();
            queue.Enqueue(new int[2] { xStart, yStart });
            Grid[xStart][yStart] = 0;
            while (queue.TryDequeue(out int[] node))
            {
                List<int[]> neigs = new List<int[]>();
                if (node[0] > 0)
                {
                    neigs.Add(new int[2] { node[0] - 1, node[1] });
                }
                if (node[1] > 0)
                {
                    neigs.Add(new int[2] { node[0], node[1] - 1 });
                }
                if (node[0] < Grid.Length - 1)
                {
                    neigs.Add(new int[2] { node[0] + 1, node[1] });
                }
                if (node[1] < Grid[0].Length - 1)
                {
                    neigs.Add(new int[2] { node[0], node[1] + 1 });
                }
                foreach (int[] neig in neigs)
                {
                    if (Grid[neig[0]][neig[1]] == 1)
                    {
                        queue.Enqueue(neig);
                        Grid[neig[0]][neig[1]] = 0;
                    }
                }
            }
        }        
    }
    public int NumEnclaves(int[][] grid) 
    {
        Grid = grid;
        int m = Grid.Length;
        int n = Grid[0].Length;

        for (int i = 0; i < m; i++)
        {
            bfs(i, 0);
            bfs(i, n - 1);
        }

        for (int j = 0; j < n; j++)
        {
            bfs(0, j);
            bfs(m - 1, j);
        }

        return Grid.SelectMany(x => x).Where(x => x == 1).Count();
    }
}
// @lc code=end

