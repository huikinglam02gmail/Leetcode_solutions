/*
 * @lc app=leetcode id=1761 lang=csharp
 *
 * [1761] Minimum Degree of a Connected Trio in a Graph
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution 
{
    public int MinTrioDegree(int n, int[][] edges) 
    {
        List<HashSet<int>> graph = new List<HashSet<int>>();
        int[] degree = new int[n];
        
        for (int i = 0; i < n; i++) 
        {
            graph.Add(new HashSet<int>());
        }
        
        foreach (int[] edge in edges) 
        {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            
            graph[u].Add(v);
            graph[v].Add(u);
            degree[u]++;
            degree[v]++;
        }
        
        int result = 3 * n;
        
        for (int i = 0; i < n - 2; i++) 
        {
            for (int j = i + 1; j < n - 1; j++) 
            {
                for (int k = j + 1; k < n; k++) 
                {
                    if (graph[i].Contains(j) && graph[i].Contains(k) && graph[j].Contains(k)) 
                    {
                        result = Math.Min(result, degree[i] + degree[j] + degree[k] - 6);
                    }
                }
            }
        }
        
        return result != 3 * n ? result : -1;
    }
}

// @lc code=end

