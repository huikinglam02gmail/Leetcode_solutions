/*
 * @lc app=leetcode id=1615 lang=csharp
 *
 * [1615] Maximal Network Rank
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximalNetworkRank(int n, int[][] roads) {
        int[] degrees = new int[n];
        foreach (int[] road in roads) {
            degrees[road[0]]++;
            degrees[road[1]]++;
        }
        
        int result = 0;
        HashSet<Tuple<int, int>> roadsSet = new HashSet<Tuple<int, int>>();
        foreach (int[] road in roads) {
            roadsSet.Add(new Tuple<int, int>(road[0], road[1]));
        }
        
        for (int node1 = 0; node1 < n - 1; node1++) {
            for (int node2 = node1 + 1; node2 < n; node2++) {
                if (roadsSet.Contains(new Tuple<int, int>(node1, node2)) || roadsSet.Contains(new Tuple<int, int>(node2, node1))) {
                    result = Math.Max(result, degrees[node1] + degrees[node2] - 1);
                } else {
                    result = Math.Max(result, degrees[node1] + degrees[node2]);
                }
            }
        }
        
        return result;
    }
}

// @lc code=end

