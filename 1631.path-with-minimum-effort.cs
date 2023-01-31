/*
 * @lc app=leetcode id=1631 lang=csharp
 *
 * [1631] Path With Minimum Effort
 */

// @lc code=start
public class Solution 
{
    public int MinimumEffortPath(int[][] heights) 
    {
        PriorityQueue<int[], int> heap = new PriorityQueue<int[], int>();
        int m = heights.Length;
        int n = heights[0].Length;
        heap.Enqueue(new int[2]{0,0}, 0);
        List<int[]> neigs = new List<int[]>();
        while (heap.TryDequeue(out int[] node, out int weight))
        {
            if (node[0] == m - 1 && node[1] == n - 1)
            {
                return weight;
            }
            else if (heights[node[0]][node[1]] >= 1)
            {
                neigs.Clear();
                neigs.Add(new int[2]{node[0], node[1] + 1});
                neigs.Add(new int[2]{node[0], node[1] - 1});
                neigs.Add(new int[2]{node[0] + 1, node[1]});
                neigs.Add(new int[2]{node[0] - 1, node[1]});
                for (int i = 0; i < 4; i++)
                {
                    int xn = neigs[i][0];
                    int yn = neigs[i][1];
                    if (xn >= 0 && xn < m && yn >= 0  && yn < n && heights[xn][yn] >= 1)
                    {
                        heap.Enqueue(neigs[i], Math.Max(weight, Math.Abs(heights[xn][yn] - heights[node[0]][node[1]])));
                    }
                }
                heights[node[0]][node[1]] = -1;
            }
        }    
        return -1;
    }
}

// @lc code=end

