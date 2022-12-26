/*
 * @lc app=leetcode id=1568 lang=csharp
 *
 * [1568] Minimum Number of Days to Disconnect Island
 */

// @lc code=start
public class Solution {
    public int NumIslands(int[][] grid) 
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int result = 0;
        Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>();
        HashSet<Tuple<int, int>> visited = new HashSet<Tuple<int, int>>();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                Tuple<int, int> t = new Tuple<int, int>(i,j);
                if (grid[i][j] == 1 && !visited.Contains(t))
                {
                    queue.Clear();
                    queue.Enqueue(t);
                    visited.Add(t);
                    while (queue.TryDequeue(out Tuple<int, int> node))
                    {
                        int nodeX = node.Item1;
                        int nodeY = node.Item2;
                        Tuple<int, int>[] nxt = new Tuple<int, int>[4]{new Tuple<int, int>(nodeX + 1, nodeY), new Tuple<int, int>(nodeX - 1, nodeY), new Tuple<int, int>(nodeX, nodeY - 1), new Tuple<int, int>(nodeX, nodeY + 1)};
                        for (int k = 0; k < 4; k++)
                        {
                            if (nxt[k].Item1 >= 0 && nxt[k].Item1 < m && nxt[k].Item2 >= 0 && nxt[k].Item2 < n && grid[nxt[k].Item1][nxt[k].Item2] == 1 && !visited.Contains(nxt[k]))
                            {
                                queue.Enqueue(nxt[k]);
                                visited.Add(nxt[k]);
                            }
                        }
                    }
                    result++;
                }
            }
        }
        return result; 
    }
    public int MinDays(int[][] grid) 
    {
        int initial = NumIslands(grid);
        if (initial != 1)
        {
            return 0;
        }    
        else
        {
            int m = grid.Length;
            int n = grid[0].Length;
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (grid[i][j] == 1)
                    {
                        grid[i][j] = 0;
                        if (NumIslands(grid) != 1)
                        {
                            return 1;
                        }
                        grid[i][j] = 1;
                    }
                }
            }
            return 2;
        }
    }
}
// @lc code=end

