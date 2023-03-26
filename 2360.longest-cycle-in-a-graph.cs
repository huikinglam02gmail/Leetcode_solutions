/*
 * @lc app=leetcode id=2360 lang=csharp
 *
 * [2360] Longest Cycle in a Graph
 */

// @lc code=start
using System.Linq;
using System.Collections.Generic;
public class Solution 
{
    public int LongestCycle(int[] edges) 
    {
        int n = edges.Length;
        List<int[]> adjacencies = new List<int[]>();
        bool[] visited = new bool[n];
        for (int i = 0; i < n; i++)
        {
            adjacencies.Add(new int[2]{0, i});
            visited[i] = false;
        }
        foreach (int edge in edges)
        {
            adjacencies[edge][0]++;
        }
        
        Queue<int[]> queue = new Queue<int[]>();
        int result = -1;
        adjacencies = adjacencies.OrderBy(x => x[0]).ToList();
        for (int i = 0; i < n; i++)
        {
            Dictionary<int, int> appeared = new Dictionary<int, int>();
            queue.Enqueue(new int[]{adjacencies[i][1], 0});
            visited[adjacencies[i][1]] = true;
            appeared.Add(adjacencies[i][1], 0);
            while (queue.TryDequeue(out int[] node))
            {
                int nxt = edges[node[0]];
                if (edges[node[0]] != -1)
                {
                    if (!visited[nxt])
                    {
                        visited[nxt] = true;
                        appeared[nxt] = node[1] + 1;
                        queue.Enqueue(new int[2]{nxt, node[1] + 1});
                    }
                }
                else if (appeared.ContainsKey(nxt))
                {
                    result = Math.Max(result, node[1] + 1 - appeared[nxt]);
                }
            }
        }
        return result;
    }
}
// @lc code=end

