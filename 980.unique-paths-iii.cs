/*
 * @lc app=leetcode id=980 lang=csharp
 *
 * [980] Unique Paths III
 */

// @lc code=start
public class Solution 
{
    int[] end;
    int result;
    int count;
    Dictionary<Tuple<int, int>, int> mapping = new Dictionary<Tuple<int, int>, int>();
    public void dfs(int row, int col, int state)
    {
        if (row == end[0] && col == end[1])
        {
            if (state == (int)Math.Pow((double) 2, (double) count) - 1)
            {
                result++;
            }
        }
        else
        {
            Tuple<int, int>[] neigs = new Tuple<int, int>[4]
            {Tuple.Create(row + 1, col), Tuple.Create(row - 1, col),
             Tuple.Create(row, col - 1), Tuple.Create(row, col + 1)};
            foreach (Tuple<int, int> neig in neigs)
            {
                if (mapping.ContainsKey(neig) && ((state & (1 << mapping[neig])) == 0))
                {
                    dfs(neig.Item1, neig.Item2, state ^ (1 << mapping[neig]));
                }
            }
        }
    }
    public int UniquePathsIII(int[][] grid) 
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int [] start = new int[2];
        int state = 0;

        count = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                Tuple<int, int> t = new Tuple<int, int>(i, j);
                if (grid[i][j] != -1)
                {
                    mapping.Add(t, count);
                    count++;
                }
                if (grid[i][j] == 1)
                {
                    start[0] = i;
                    start[1] = j;
                    state = 1 << (count - 1);
                }
                if (grid[i][j] == 2)
                {
                    end = new int[2]{i, j};
                }     
            }
        }
        result = 0;
        dfs(start[0], start[1], state);
        return result;
    }
}
// @lc code=end

