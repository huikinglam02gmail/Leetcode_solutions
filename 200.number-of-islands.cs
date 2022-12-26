/*
 * @lc app=leetcode id=200 lang=csharp
 *
 * [200] Number of Islands
 */

// @lc code=start
public class Solution 
{
    public int NumIslands(char[][] grid) 
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int result = 0;
        Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == '1')
                {
                    queue.Clear();
                    queue.Enqueue(new Tuple<int, int>(i, j));
                    grid[i][j] = '0';
                    while (queue.TryDequeue(out Tuple<int, int> node))
                    {
                        int nodeX = node.Item1;
                        int nodeY = node.Item2;
                        Tuple<int, int>[] nxt = new Tuple<int, int>[4]{new Tuple<int, int>(nodeX + 1, nodeY), new Tuple<int, int>(nodeX - 1, nodeY), new Tuple<int, int>(nodeX, nodeY - 1), new Tuple<int, int>(nodeX, nodeY + 1)};
                        for (int k = 0; k < 4; k++)
                        {
                            if (nxt[k].Item1 >= 0 && nxt[k].Item1 < m && nxt[k].Item2 >= 0 && nxt[k].Item2 < n && grid[nxt[k].Item1][nxt[k].Item2] == '1')
                            {
                                queue.Enqueue(nxt[k]);
                                grid[nxt[k].Item1][nxt[k].Item2] = '0';
                            }
                        }
                    }
                    result++;
                }
            }
        }
        return result; 
    }
}
// @lc code=end

