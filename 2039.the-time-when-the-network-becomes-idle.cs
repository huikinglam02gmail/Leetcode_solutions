/*
 * @lc app=leetcode id=2039 lang=csharp
 *
 * [2039] The Time When the Network Becomes Idle
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int NetworkBecomesIdle(int[][] edges, int[] patience) {
        int n = patience.Length;
        int[] dist = new int[n];
        bool[] visited = new bool[n];
        List<HashSet<int>> graph = new List<HashSet<int>>(n);
        for (int i = 0; i < n; i++) {
            graph.Add(new HashSet<int>());
        }

        foreach (var edge in edges) {
            int u = edge[0];
            int v = edge[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }

        Queue<int> dq = new Queue<int>();
        dq.Enqueue(0);
        visited[0] = true;
        int steps = 0;

        while (dq.Count > 0) {
            int count = dq.Count;
            for (int i = 0; i < count; i++) {
                int node = dq.Dequeue();
                dist[node] = steps;
                foreach (int nxt in graph[node]) {
                    if (!visited[nxt]) {
                        dq.Enqueue(nxt);
                        visited[nxt] = true;
                    }
                }
            }
            steps += 2;
        }

        int result = 0;
        for (int i = 1; i < n; i++) {
            int lastOut = ((dist[i] - 1) / patience[i]) * patience[i];
            result = Math.Max(result, dist[i] + 1 + lastOut);
        }

        return result;
    }
}

// @lc code=end

