/*
 * @lc app=leetcode id=2492 lang=csharp
 *
 * [2492] Minimum Score of a Path Between Two Cities
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
public class Solution 
{
    public int MinScore(int n, int[][] roads) 
    {
        HashSet<int>[] graph = new HashSet<int>[n];
        graph = graph.Select(x => new HashSet<int>()).ToArray();
        foreach (int[] road in roads)
        {
            graph[road[0] - 1].Add(road[1] - 1);
            graph[road[1] - 1].Add(road[0] - 1);
        }

        Queue<int> queue = new Queue<int>();
        HashSet<int> visited = new HashSet<int>();
        queue.Enqueue(0);
        visited.Add(0);
        while (queue.TryDequeue(out int node))
        {
            foreach (int nxt in graph[node])
            {
                if (!visited.Contains(nxt))
                {
                    queue.Enqueue(nxt);
                    visited.Add(nxt);
                }
            }
        }

        int minSoFar = 10000;
        foreach(int[] road in roads)
        {
            if (visited.Contains(road[0] - 1))
            {
                minSoFar = Math.Min(minSoFar, road[2]);
            }
        }   
        return minSoFar;
    }
}
// @lc code=end

