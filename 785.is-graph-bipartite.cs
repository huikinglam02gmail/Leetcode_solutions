/*
 * @lc app=leetcode id=785 lang=csharp
 *
 * [785] Is Graph Bipartite?
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    public bool IsBipartite(int[][] graph) 
    {
        int n = graph.Length;
        int[] inSet = new int[n];
        Array.Fill(inSet, -1);

        Queue<int> queue = new Queue<int>();
        for (int i = 0; i < n; i++)
        {
            if (inSet[i] == -1)
            {
                queue.Clear();
                queue.Enqueue(i);
                inSet[i] = 0;
                while (queue.TryDequeue(out int node))
                {
                    foreach (int j in graph[node])
                    {
                        if (inSet[j] == inSet[node])
                        {
                            return false;
                        }
                        else if (inSet[j] == -1)
                        {
                            inSet[j] = 1 - inSet[node];
                            queue.Enqueue(j);
                        }
                    }
                }
            }
        }
        return true;
    }
}
// @lc code=end

