/*
 * @lc app=leetcode id=2092 lang=csharp
 *
 * [2092] Find All People With Secret
 */

// @lc code=start
using System.Collections.Generic;

public class UnionFindSet {
    private int[] parents;
    public int Count { get; private set; }

    public UnionFindSet(int n) {
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        Count = n;
    }

    public int Find(int u) {
        if (u != parents[u]) {
            parents[u] = Find(parents[u]);
        }
        return parents[u];
    }

    public void Union(int u, int v) {
        int pu = Find(u);
        int pv = Find(v);
        if (pu != pv) {
            parents[Math.Max(pu, pv)] = Math.Min(pu, pv);
            Count--;
        }
    }
}

public class Solution {
    public int[] FindAllPeople(int n, int[][] meetings, int firstPerson) {
        List<int[]> sortedMeetings = new List<int[]>(meetings);
        sortedMeetings.Insert(0, new int[] { 0, firstPerson, 0 });
        sortedMeetings.Sort((a, b) => a[2] - b[2]);

        UnionFindSet UF = new UnionFindSet(n + 1);
        int i = 0;
        int t = 0;
        while (i < sortedMeetings.Count) {
            t = sortedMeetings[i][2];
            Dictionary<int, HashSet<int>> graph = new Dictionary<int, HashSet<int>>();
            Queue<int> dq = new Queue<int>();
            HashSet<int> visited = new HashSet<int>();
            while (i < sortedMeetings.Count && t == sortedMeetings[i][2]) {
                int u = sortedMeetings[i][0];
                int v = sortedMeetings[i][1];
                if (!graph.ContainsKey(u)) graph[u] = new HashSet<int>();
                if (!graph.ContainsKey(v)) graph[v] = new HashSet<int>();
                graph[u].Add(v);
                graph[v].Add(u);
                if (UF.Find(u) == 0 && !visited.Contains(u)) {
                    dq.Enqueue(u);
                    visited.Add(u);
                }
                if (UF.Find(v) == 0 && !visited.Contains(v)) {
                    dq.Enqueue(v);
                    visited.Add(v);
                }
                i++;
            }
            while (dq.Count > 0) {
                int node = dq.Dequeue();
                foreach (int nxt in graph[node]) {
                    if (!visited.Contains(nxt)) {
                        if (UF.Find(nxt) > 0) {
                            UF.Union(0, nxt);
                        }
                        dq.Enqueue(nxt);
                        visited.Add(nxt);
                    }
                }
            }
        }
        List<int> result = new List<int>();
        for (int j = 0; j <= n; j++) {
            if (UF.Find(j) == 0) result.Add(j);
        }
        return result.ToArray();
    }
}

// @lc code=end

