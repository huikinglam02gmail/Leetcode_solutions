/*
 * @lc app=leetcode id=1857 lang=csharp
 *
 * [1857] Largest Color Value in a Directed Graph
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
using System;
public class Solution 
{
    public int LargestPathValue(string colors, int[][] edges) 
    {
        int n = colors.Length;
        HashSet<int>[] graph = new HashSet<int>[n];
        graph = graph.Select(x => new HashSet<int>()).ToArray();
        int[] adjacency = new int[n];
        Array.Fill(adjacency, 0);
        int result = -1;
        int[][] colorValues = new int[n][];
        colorValues = colorValues.Select(x => Enumerable.Repeat(0, 26).ToArray()).ToArray();

        foreach (int[] edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            adjacency[edge[1]]++;
        }

        Queue<int> queue = new Queue<int>();
        for (int i = 0; i < n; i++)
        {
            if (adjacency[i] == 0)
            {
                queue.Enqueue(i);
            }
        }

        while (queue.TryDequeue(out int node))
        {
            colorValues[node][(int)colors[node] - (int)'a']++;
            result = Math.Max(result, colorValues[node][(int)colors[node] - (int)'a']);
            foreach (int nxt in graph[node])
            {
                for (int j = 0; j < 26; j++)
                {
                    colorValues[nxt][j] = Math.Max(colorValues[nxt][j], colorValues[node][j]);
                }
                adjacency[nxt]--;
                if (adjacency[nxt] == 0)
                {
                    queue.Enqueue(nxt);
                }
            }
        }

        return adjacency.Sum() > 0 ? -1 : result;
    }
}
// @lc code=end

