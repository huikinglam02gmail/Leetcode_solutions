/*
 * @lc app=leetcode id=2050 lang=csharp
 *
 * [2050] Parallel Courses III
 */

// @lc code=start
/**
 * @lc app=leetcode id=2050 lang=csharp
 *
 * [2050] Parallel Courses III
 */

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTime(int n, int[][] relations, int[] time) {
        List<HashSet<int>> graph = new List<HashSet<int>>(n);
        int[] adj = new int[n];

        for (int i = 0; i < n; i++) {
            graph.Add(new HashSet<int>());
        }

        foreach (var relation in relations) {
            int prev = relation[0] - 1;
            int next = relation[1] - 1;
            graph[prev].Add(next);
            adj[next]++;
        }

        int[] dp = new int[n];
        Queue<int> queue = new Queue<int>();

        for (int i = 0; i < n; i++) {
            if (adj[i] == 0) {
                queue.Enqueue(i);
            }
        }

        while (queue.Count > 0) {
            int course = queue.Dequeue();
            foreach (int next in graph[course]) {
                dp[next] = Math.Max(dp[next], dp[course] + time[course]);
                adj[next]--;
                if (adj[next] == 0) {
                    queue.Enqueue(next);
                }
            }
        }

        int maxTime = 0;
        for (int i = 0; i < n; i++) {
            maxTime = Math.Max(maxTime, dp[i] + time[i]);
        }

        return maxTime;
    }
}

// @lc code=end

