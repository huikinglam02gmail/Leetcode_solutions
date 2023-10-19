/*
 * @lc app=leetcode id=1948 lang=csharp
 *
 * [1948] Delete Duplicate Folders in System
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    private List<List<string>> paths;
    private List<List<int>> graph;
    private Dictionary<string, HashSet<int>> subtreeIndexMap;
    private HashSet<int> keysToThrow;

    public IList<IList<string>> DeleteDuplicateFolder(IList<IList<string>> paths) {
        int n = paths.Count;
        var data = new List<int[]>();

        for (int i = 0; i < n; i++) {
            data.Add(new int[] { paths[i].Count, i });
        }

        data.Sort((a, b) => a[0] - b[0]);

        this.paths = paths.Select(path => new List<string>(path)).ToList();
        int m = data[data.Count - 1][0];

        this.graph = new List<List<int>>();
        for (int i = 0; i < n; i++) {
            this.graph.Add(new List<int>());
        }

        int j = 0;
        int cur = 0;
        var prev = new HashSet<string>();
        var serializedPathToIndex = new Dictionary<string, int>();
        this.subtreeIndexMap = new Dictionary<string, HashSet<int>>();
        var dfsStartNodes = new HashSet<int>();

        while (j < n) {
            cur++;
            var next = new HashSet<string>();

            while (j < n && data[j][0] == cur) {
                var pathSerialized = string.Join(",", this.paths[data[j][1]]);
                var parentSerialized = string.Join(",", this.paths[data[j][1]].Take(this.paths[data[j][1]].Count - 1));

                if (prev.Contains(parentSerialized)) {
                    this.graph[serializedPathToIndex[parentSerialized]].Add(data[j][1]);
                }

                serializedPathToIndex[pathSerialized] = data[j][1];
                next.Add(pathSerialized);
                j++;
            }

            if (cur == 1) {
                foreach (var nextPath in next) {
                    dfsStartNodes.Add(serializedPathToIndex[nextPath]);
                }
            }

            prev = next;
        }

        foreach (var node in dfsStartNodes) {
            this.Dfs(node);
        }

        this.keysToThrow = new HashSet<int>();
        foreach (var indices in this.subtreeIndexMap.Values) {
            if (indices.Count > 1) {
                foreach (var i in indices) {
                    if (!this.keysToThrow.Contains(i)) {
                        this.DfsThrow(i);
                    }
                }
            }
        }

        var result = new List<IList<string>>();
        for (int i = 0; i < n; i++) {
            if (!this.keysToThrow.Contains(i)) {
                result.Add(this.paths[i]);
            }
        }

        return result;
    }

    private string Dfs(int node) {
        var n = this.graph[node].Count;
        var nodesSorted = this.graph[node].OrderBy(x => this.paths[x].Last()).ToList();
        var result = "";
        
        if (n > 0) {
            result += ":";
        }

        if (n > 1) {
            result += "[";
        }

        for (int i = 0; i < n; i++) {
            result += "{";
            result += this.Dfs(nodesSorted[i]);
            result += "}";

            if (i < n - 1) {
                result += ",";
            }
        }

        if (n > 1) {
            result += "]";
        }

        if (!string.IsNullOrEmpty(result)) {
            if (!this.subtreeIndexMap.ContainsKey(result)) {
                this.subtreeIndexMap[result] = new HashSet<int>();
            }

            this.subtreeIndexMap[result].Add(node);
        }
        
        return this.paths[node][this.paths[node].Count - 1] + result;
    }

    private void DfsThrow(int node) {
        this.keysToThrow.Add(node);

        foreach (var child in this.graph[node]) {
            if (!this.keysToThrow.Contains(child)) {
                this.DfsThrow(child);
            }
        }
    }
}

// @lc code=end

