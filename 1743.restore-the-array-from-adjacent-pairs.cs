/*
 * @lc app=leetcode id=1743 lang=csharp
 *
 * [1743] Restore the Array From Adjacent Pairs
 */

// @lc code=start
using System.Collections.Generic;

public class Solution
{
    public int[] RestoreArray(int[][] adjacentPairs)
    {
        Dictionary<int, HashSet<int>> graph = new Dictionary<int, HashSet<int>>();

        foreach (int[] pair in adjacentPairs)
        {
            int a = pair[0];
            int b = pair[1];

            if (!graph.ContainsKey(a))
            {
                graph[a] = new HashSet<int>();
            }

            if (!graph.ContainsKey(b))
            {
                graph[b] = new HashSet<int>();
            }

            graph[a].Add(b);
            graph[b].Add(a);
        }

        int start = 0;
        foreach (int key in graph.Keys)
        {
            if (graph[key].Count == 1)
            {
                start = key;
                break;
            }
        }

        Queue<int> queue = new Queue<int>();
        HashSet<int> visited = new HashSet<int>();
        queue.Enqueue(start);
        visited.Add(start);
        List<int> result = new List<int>();

        while (queue.Count > 0)
        {
            result.Add(queue.Dequeue());

            foreach (int next in graph[result[result.Count - 1]])
            {
                if (!visited.Contains(next))
                {
                    queue.Enqueue(next);
                    visited.Add(next);
                }
            }
        }

        return result.ToArray();
    }
}

// @lc code=end

