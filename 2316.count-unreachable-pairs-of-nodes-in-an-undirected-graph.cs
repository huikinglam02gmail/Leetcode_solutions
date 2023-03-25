/*
 * @lc app=leetcode id=2316 lang=csharp
 *
 * [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
using System;
public class Solution 
{
    public long CountPairs(int n, int[][] edges) 
    {
        HashSet<int>[] graph = new HashSet<int>[n];
        graph = graph.Select(x => new HashSet<int>()).ToArray();
        foreach (int[] edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }

        List<int> groupCounts = new List<int>();
        bool[] visited = new bool[n];
        Array.Fill(visited, false);
        Queue<int> queue = new Queue<int>();
        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                int count = 0;
                queue.Enqueue(i);
                visited[i] = true;
                while (queue.TryDequeue(out int node))
                {
                    count++;
                    foreach (int nxt in graph[node])
                    {
                        if (!visited[nxt])
                        {
                            visited[nxt] = true;
                            queue.Enqueue(nxt);
                        }
                    }
                }
                groupCounts.Add(count);
            }
        }

        long total = groupCounts.Sum();
        long result = 0;
        foreach (int count in groupCounts)
        {
            result += count * (total - count);
        }
        return result / 2;
    }
}
// @lc code=end

