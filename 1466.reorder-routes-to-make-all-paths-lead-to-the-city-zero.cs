/*
 * @lc app=leetcode id=1466 lang=csharp
 *
 * [1466] Reorder Routes to Make All Paths Lead to the City Zero
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
using System;
public class Solution 
{
    public int MinReorder(int n, int[][] connections) 
    {
        HashSet<Tuple<int, int>>[] graph = new HashSet<Tuple<int, int>>[n];
        graph = graph.Select(x => new HashSet<Tuple<int, int>>()).ToArray();
        for (int i = 0; i < connections.Length; i++)
        {
            graph[connections[i][0]].Add(new Tuple<int, int>(connections[i][1], i));
            graph[connections[i][1]].Add(new Tuple<int, int>(connections[i][0], i));
        }

        Queue<int> queue = new Queue<int>();
        int result = 0;
        bool[] visited = new bool[n];
        Array.Fill(visited, false);
        queue.Enqueue(0);
        visited[0] = true;
        while(queue.TryDequeue(out int node))
        {
            foreach (Tuple<int, int> t in graph[node])
            {
                if (!visited[t.Item1])
                {
                    if (connections[t.Item2][0] == node && connections[t.Item2][1] == t.Item1)
                    {
                        result++;
                    }
                    queue.Enqueue(t.Item1);
                    visited[t.Item1] = true;
                }
            }
        }
        return result;   
    }
}
// @lc code=end

