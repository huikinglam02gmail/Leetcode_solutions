/*
 * @lc app=leetcode id=1786 lang=csharp
 *
 * [1786] Number of Restricted Paths From First to Last Node
 */

// @lc code=start
public class Solution {
    private int[] Dijkstra(Dictionary<int, int>[] graph, int source)
    {
        int n = graph.Length;
        int[] result = new int[n];
        Array.Fill(result, -1);

        PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
        bool[] visited = new bool[n];
        Array.Fill(visited, false);
        int visitedCount = 0;
        heap.Enqueue(source, 0);

        while (heap.TryDequeue(out int node, out int weight) && visitedCount < n)
        {
            if (result[node] < 0)
            {
                result[node] = weight;
                visited[node] = true;
                visitedCount++;
                foreach (int nxt in graph[node].Keys)
                {
                    heap.Enqueue(nxt, weight + graph[node][nxt]);
                }
            }
        }
        return result;
    }        
    const private long MOD = 1000000007; 
    public int CountRestrictedPaths(int n, int[][] edges) {
        Dictionary<int, int>[] graph = new Dictionary<int, int>[n];
        foreach (int[] edge in edges)
        {
            graph[edge[0] - 1].Add(edge[1] - 1, edge[2]);
            graph[edge[1] - 1].Add(edge[0] - 1, edge[2]);
        }
    }
}
// @lc code=end

