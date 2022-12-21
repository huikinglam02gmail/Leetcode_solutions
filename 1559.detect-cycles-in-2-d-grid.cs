/*
 * @lc app=leetcode id=1559 lang=csharp
 *
 * [1559] Detect Cycles in 2D Grid
 */

// @lc code=start
public class Solution 
{
    public bool ContainsCycle(char[][] grid) 
    {
        int m = grid.Length;
        int n = grid[0].Length;
        HashSet<Tuple<int, int>> visited = new HashSet<Tuple<int, int>>();
        Queue<Tuple<int, int, int, int>> queue = new Queue<Tuple<int, int, int, int>>();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!visited.Contains(Tuple.Create(i,j)))
                {
                    queue.Clear();
                    queue.Enqueue(Tuple.Create(i, j, -1, -1));
                    visited.Add(Tuple.Create(i, j));
                    while (queue.TryDequeue(out Tuple<int, int, int, int> t))
                    {
                        Tuple<int, int, int, int>[] neigs = new Tuple<int, int, int, int>[4];
                        neigs[0] = Tuple.Create(t.Item1 + 1, t.Item2, t.Item1, t.Item2);
                        neigs[1] = Tuple.Create(t.Item1 - 1, t.Item2, t.Item1, t.Item2);
                        neigs[2] = Tuple.Create(t.Item1, t.Item2 - 1, t.Item1, t.Item2);
                        neigs[3] = Tuple.Create(t.Item1, t.Item2 + 1, t.Item1, t.Item2);
                        foreach (Tuple<int, int, int, int> nxt in neigs)
                        {
                            if (nxt.Item1 >= 0 && nxt.Item1 < m && nxt.Item2 >= 0 && nxt.Item2 < n && (nxt.Item1 != t.Item3 || nxt.Item2 != t.Item4) && grid[nxt.Item1][nxt.Item2] == grid[i][j])
                            {
                                if (visited.Contains(Tuple.Create(nxt.Item1, nxt.Item2)))
                                {
                                    return true;
                                }
                                else
                                {
                                    queue.Enqueue(nxt);
                                    visited.Add(Tuple.Create(nxt.Item1, nxt.Item2));
                                }
                            }
                        }
                    }
                }
            }
        }
        return false;
    }
}
// @lc code=end

