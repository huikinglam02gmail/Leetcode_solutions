/*
 * @lc app=leetcode id=2045 lang=csharp
 *
 * [2045] Second Minimum Time to Reach Destination
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int SecondMinimum(int n, int[][] edges, int time, int change) {
        int[][] minimumTime = new int[n][];
        for (int i = 0; i < n; i++) {
            minimumTime[i] = new int[] { int.MaxValue, int.MaxValue };
        }

        HashSet<int>[] graph = new HashSet<int>[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new HashSet<int>();
        }

        foreach (var edge in edges) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            graph[u].Add(v);
            graph[v].Add(u);
        }

        minimumTime[0][0] = 0;
        Queue<int[]> dq = new Queue<int[]>();
        dq.Enqueue(new int[] { 0, 0 });

        while (dq.Count > 0) {
            int[] current = dq.Dequeue();
            int node = current[0];
            int t = current[1];

            if ((t / change) % 2 == 1) {
                t = ((t / change) + 1) * change;
            }

            foreach (int nxt in graph[node]) {
                int nxtTime = t + time;

                if (minimumTime[nxt][0] > nxtTime) {
                    minimumTime[nxt][0] = nxtTime;
                    dq.Enqueue(new int[] { nxt, nxtTime });
                } else if (minimumTime[nxt][0] < nxtTime && nxtTime < minimumTime[nxt][1]) {
                    minimumTime[nxt][1] = nxtTime;
                    dq.Enqueue(new int[] { nxt, nxtTime });
                }
            }
        }

        return minimumTime[n - 1][1];
    }
}

// @lc code=end

