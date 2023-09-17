/*
 * @lc app=leetcode id=847 lang=csharp
 *
 * [847] Shortest Path Visiting All Nodes
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int ShortestPathLength(int[][] graph) {
        Queue<(int node, int mask)> queue = new Queue<(int, int)>();
        HashSet<(int node, int mask)> visited = new HashSet<(int, int)>();
        int n = graph.Length;
        int steps = 0;

        for (int i = 0; i < n; i++) {
            queue.Enqueue((i, 1 << i));
            visited.Add((i, 1 << i));
        }

        while (queue.Count > 0) {
            int queueSize = queue.Count;

            for (int i = 0; i < queueSize; i++) {
                (int node, int mask) = queue.Dequeue();

                if (mask == (1 << n) - 1) {
                    return steps;
                }

                foreach (int neighbor in graph[node]) {
                    int newMask = mask | (1 << neighbor);

                    if (!visited.Contains((neighbor, newMask))) {
                        queue.Enqueue((neighbor, newMask));
                        visited.Add((neighbor, newMask));
                    }
                }
            }

            steps++;
        }

        return -1; // Should not reach here
    }
}

// @lc code=end

