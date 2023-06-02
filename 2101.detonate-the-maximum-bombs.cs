/*
 * @lc app=leetcode id=2101 lang=csharp
 *
 * [2101] Detonate the Maximum Bombs
 */

// @lc code=start
using System.Collections.Generic;
using System;

public class Solution
{
    /*
    Build the graph first, then BFS from every bomb and find how many it can reach
    */
    private int BfsLargestClusterSize(List<HashSet<int>> graph)
    {
        int n = graph.Count;
        int result = 0;
        for (int i = 0; i < n; i++)
        {
            Queue<int> dq = new Queue<int>();
            HashSet<int> local = new HashSet<int>();
            dq.Enqueue(i);
            local.Add(i);
            while (dq.Count > 0)
            {
                int node = dq.Dequeue();
                foreach (int nxt in graph[node])
                {
                    if (!local.Contains(nxt))
                    {
                        local.Add(nxt);
                        dq.Enqueue(nxt);
                    }
                }
            }
            result = Math.Max(result, local.Count);
        }
        return result;
    }

    public int MaximumDetonation(int[][] bombs)
    {
        int n = bombs.Length;
        List<HashSet<int>> graph = new List<HashSet<int>>();
        for (int i = 0; i < n; i++)
        {
            graph.Add(new HashSet<int>());
        }

        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                int distX = bombs[i][0] - bombs[j][0];
                int distY = bombs[i][1] - bombs[j][1];
                if (Convert.ToInt64(distX) * Convert.ToInt64(distX) + Convert.ToInt64(distY) * Convert.ToInt64(distY) <= Convert.ToInt64(bombs[i][2]) * Convert.ToInt64(bombs[i][2]))
                {
                    graph[i].Add(j);
                }
                if (Convert.ToInt64(distX) * Convert.ToInt64(distX) + Convert.ToInt64(distY) * Convert.ToInt64(distY) <= Convert.ToInt64(bombs[j][2]) * Convert.ToInt64(bombs[j][2]))
                {
                    graph[j].Add(i);
                }
            }
        }
        return BfsLargestClusterSize(graph);
    }
}

// @lc code=end

