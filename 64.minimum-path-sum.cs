/*
 * @lc app=leetcode id=64 lang=csharp
 *
 * [64] Minimum Path Sum
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int MinPathSum(int[][] grid) 
    {
        PriorityQueue<int[], int> queue = new PriorityQueue<int[], int>();
        queue.Enqueue(new int[2]{0, 0}, grid[0][0]);
        grid[0][0] = -1;
        int m = grid.Length;
        int n = grid[0].Length;
        while (queue.TryDequeue(out int[] node, out int cost))
        {
            if (node[0] == m - 1 && node[1] == n - 1)
            {
                return cost;
            }
            if (node[0] < m - 1 && grid[node[0] + 1][node[1]] >= 0)
            {
                queue.Enqueue(new int[2]{node[0] + 1, node[1]}, cost + grid[node[0] + 1][node[1]]);
                grid[node[0] + 1][node[1]] = -1;
            }
            if (node[1] < n - 1 && grid[node[0]][node[1] + 1] >= 0)
            {
                queue.Enqueue(new int[2]{node[0], node[1] + 1}, cost + grid[node[0]][node[1] + 1]);
                grid[node[0]][node[1]+ 1] = -1;
            }
        }    
        return -1;
    }
}
// @lc code=end

