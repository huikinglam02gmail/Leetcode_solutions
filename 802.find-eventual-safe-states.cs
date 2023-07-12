/*
 * @lc app=leetcode id=802 lang=csharp
 *
 * [802] Find Eventual Safe States
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    DFS solution
    Safe nodes = nodes not in cycle
    Strategy: DFS from each node and record the path nodes when a cycle is detected
    For a node to be safe, all the path went out from it do not encounter a cycle
    When conducting DFS, we do not need to search nodes previously proven to be safe
    Also, we do not search the known cycle nodes
    */
    private HashSet<int> safeNodes;
    private HashSet<int> cycleNodes;
    private List<List<int>> graph;

    private bool DFS(int node, List<int> path) {
        if (path.Contains(node)) {
            foreach (int item in path) {
                cycleNodes.Add(item);
            }
            return false;
        } else {
            foreach (int nxt in graph[node]) {
                if (!safeNodes.Contains(nxt) && !DFS(nxt, new List<int>(path) { node })) {
                    return false;
                }
            }
            safeNodes.Add(node);
            return true;
        }
    }

    public IList<int> EventualSafeNodes(IList<IList<int>> graph) {
        this.graph = new List<List<int>>();
        foreach (IList<int> neighbors in graph) {
            this.graph.Add(new List<int>(neighbors));
        }

        safeNodes = new HashSet<int>();
        cycleNodes = new HashSet<int>();

        for (int i = 0; i < graph.Count; i++) {
            if (!cycleNodes.Contains(i)) {
                DFS(i, new List<int>());
            }
        }

        List<int> result = new List<int>(safeNodes);
        result.Sort();
        return result;
    }
}

// @lc code=end

