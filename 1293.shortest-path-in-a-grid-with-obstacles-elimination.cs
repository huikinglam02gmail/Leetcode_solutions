/*
 * @lc app=leetcode id=1293 lang=csharp
 *
 * [1293] Shortest Path in a Grid with Obstacles Elimination
 */

// @lc code=start
public class Solution {
    public int ShortestPath(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int steps = 0;
        Queue<int[]> queue = new Queue<int[]>();
        Dictionary<Tuple<int,int>, int> visited = new Dictionary<Tuple<int,int>, int>();
        queue.Enqueue(new int[3]{0, 0, 0});
        visited[new Tuple<int,int>(0,0)] = 0;
        while (queue.Count > 0)
        {
            int l = queue.Count;
            for (int i = 0; i < l; i++)
            {
                int[] item = queue.Dequeue();
                //Console.WriteLine($"{item[0]}, {item[1]}, {item[2]}");
                if (item[0] == m-1 && item[1] == n-1)
                {
                    return steps;
                }
                int[][] neigs = new int[4][];
                neigs[0] = new int[]{item[0]-1, item[1]};
                neigs[1] = new int[]{item[0]+1, item[1]};
                neigs[2] = new int[]{item[0], item[1]-1};
                neigs[3] = new int[]{item[0], item[1]+1};
                foreach (int[] nxt in neigs)
                {
                    int xn = nxt[0];
                    int yn = nxt[1];
                    if (xn >= 0 && xn < m && yn >= 0 && yn < n)
                    {
                        int state = item[2];
                        if (grid[xn][yn] == 1)
                        {
                            state += 1;
                        }
                        Tuple<int,int> newKey = new Tuple<int,int>(xn,yn);
                        if (state <= k && (!visited.ContainsKey(newKey) || visited[newKey] > state))
                        {
                            queue.Enqueue(new int[3]{xn, yn, state});
                            visited[newKey] = state;
                        }
                    }
                }
            }
            steps += 1;
        }
        return -1;
    }
}

// @lc code=end

