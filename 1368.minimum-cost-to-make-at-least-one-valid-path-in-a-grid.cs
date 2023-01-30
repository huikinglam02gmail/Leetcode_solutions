/*
 * @lc app=leetcode id=1368 lang=csharp
 *
 * [1368] Minimum Cost to Make at Least One Valid Path in a Grid
 */

// @lc code=start
public class Solution 
{
    public int MinCost(int[][] grid) 
    {
        PriorityQueue<int[], int> heap = new PriorityQueue<int[], int>();
        int m = grid.Length;
        int n = grid[0].Length;
        heap.Enqueue(new int[2]{0,0}, 0);
        List<int[]> neigs = new List<int[]>();
        while (heap.TryDequeue(out int[] node, out int weight))
        {
            if (node[0] == m - 1 && node[1] == n - 1)
            {
                return weight;
            }
            neigs.Clear();
            neigs.Add(new int[2]{node[0], node[1] + 1});
            neigs.Add(new int[2]{node[0], node[1] - 1});
            neigs.Add(new int[2]{node[0] + 1, node[1]});
            neigs.Add(new int[2]{node[0] - 1, node[1]});
            for (int i = 0; i < 4; i++)
            {
                int xn = neigs[i][0];
                int yn = neigs[i][1];
                if (xn >= 0 && xn < m && yn >=0  && yn < n && grid[xn][yn] >=  1 && grid[xn][yn] <= 4)
                {
                    if (i == grid[node[0]][node[1]] - 1)
                    {
                        heap.Enqueue(neigs[i], weight);
                    }
                    else
                    {
                        heap.Enqueue(neigs[i], weight + 1);
                    }
                }
            }
            grid[node[0]][node[1]] = 5;
        }    
        return -1;
    }
}
// @lc code=end

