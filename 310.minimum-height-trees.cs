/*
 * @lc app=leetcode id=310 lang=csharp
 *
 * [310] Minimum Height Trees
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    There can only be up to two possible roots. Just bfs from leaves until only <= 2 nodes remaining
    */
    public IList<int> FindMinHeightTrees(int n, int[][] edges) {
        if (edges.Length == 0) {
            return new List<int>(){0};
        } else if (edges.Length == 1) {
            return new List<int>(){0, 1};
        } else {
            List<HashSet<int>> neighbors = new List<HashSet<int>>();
            for (int i = 0; i < n; i++) {
                neighbors.Add(new HashSet<int>());
            }
            foreach (var edge in edges) {
                neighbors[edge[0]].Add(edge[1]);
                neighbors[edge[1]].Add(edge[0]);
            }
            List<int> leaves = new List<int>();
            for (int i = 0; i < n; i++) {
                if (neighbors[i].Count == 1) leaves.Add(i);
            }
            int remaining = n;
            while (remaining > 2) {
                List<int> newLeaves = new List<int>();
                while (leaves.Count > 0) {
                    int leaf = leaves[leaves.Count - 1];
                    leaves.RemoveAt(leaves.Count - 1);
                    int neighbor = neighbors[leaf].FirstOrDefault(); // simply connected, only 1 neighbour left
                    neighbors[leaf].Remove(neighbor);
                    remaining--;
                    neighbors[neighbor].Remove(leaf);
                    if (neighbors[neighbor].Count == 1) newLeaves.Add(neighbor);
                }
                leaves = newLeaves;
            }
            return leaves;
        }
    }
}

// @lc code=end

