/*
 * @lc app=leetcode id=2049 lang=csharp
 *
 * [2049] Count Nodes With the Highest Score
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int CountHighestScoreNodes(int[] parents) {
        int n = parents.Length;
        HashSet<int>[] children = new HashSet<int>[n];
        int[] offsprings = new int[n];
        for (int i = 0; i < n; i++) {
            children[i] = new HashSet<int>();
        }

        for (int i = 0; i < n; i++) {
            if (parents[i] >= 0) {
                children[parents[i]].Add(i);
                offsprings[parents[i]]++;
            }
        }

        int[] subtreeSize = new int[n];
        Array.Fill(subtreeSize, 1);
        Queue<int> dq = new Queue<int>();
        for (int i = 0; i < n; i++) {
            if (offsprings[i] == 0) {
                dq.Enqueue(i);
            }
        }

        while (dq.Count > 0) {
            int node = dq.Dequeue();
            if (parents[node] >= 0) {
                offsprings[parents[node]]--;
                subtreeSize[parents[node]] += subtreeSize[node];
                if (offsprings[parents[node]] == 0) {
                    dq.Enqueue(parents[node]);
                }
            }
        }

        Dictionary<long, int> counts = new Dictionary<long, int>();
        for (int i = 0; i < n; i++) {
            long score = 1;
            foreach (int child in children[i]) {
                score *= subtreeSize[child];
            }
            if (parents[i] >= 0) {
                score *= n - subtreeSize[i];
            }
            counts[score] = counts.ContainsKey(score) ? counts[score] + 1 : 1;
        }

        return counts[counts.Keys.Max()];
    }
}

// @lc code=end

