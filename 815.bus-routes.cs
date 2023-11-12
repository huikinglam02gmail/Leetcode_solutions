/*
 * @lc app=leetcode id=815 lang=csharp
 *
 * [815] Bus Routes
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int NumBusesToDestination(int[][] routes, int source, int target) {
        if (source == target)
            return 0;

        int n = routes.Length;
        HashSet<int>[] stations = new HashSet<int>[n];
        for (int i = 0; i < n; i++) {
            stations[i] = new HashSet<int>(routes[i]);
        }

        HashSet<int>[] graph = new HashSet<int>[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new HashSet<int>();
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stations[i].Overlaps(stations[j])) {
                    graph[i].Add(j);
                    graph[j].Add(i);
                }
            }
        }

        Queue<int> queue = new Queue<int>();
        bool[] visited = new bool[n];
        int steps = 1;

        for (int i = 0; i < n; i++) {
            if (stations[i].Contains(source)) {
                visited[i] = true;
                queue.Enqueue(i);
            }
        }

        while (queue.Count > 0) {
            int count = queue.Count;
            for (int i = 0; i < count; i++) {
                int route = queue.Dequeue();
                if (stations[route].Contains(target)) {
                    return steps;
                }
                foreach (int next in graph[route]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.Enqueue(next);
                    }
                }
            }
            steps++;
        }

        return -1;
    }
}

// @lc code=end

