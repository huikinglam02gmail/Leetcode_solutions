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
    private const long MOD = 1000000007;

    public int CountRestrictedPaths(int n, int[][] edges)
    {
        Dictionary<int, int>[] graph = new Dictionary<int, int>[n];
        graph = graph.Select(x => new Dictionary<int, int>()).ToArray();

        foreach (int[] edge in edges)
        {
            int a = edge[0] - 1;
            int b = edge[1] - 1;
            int w = edge[2];
            graph[a][b] = w;
            graph[b][a] = w;
        }

        int[] distanceToLastNode = Dijkstra(graph, n - 1);
        List<Tuple<int, int>> distanceToLastNodeSorted = distanceToLastNode
            .Select((distance, index) => new Tuple<int, int>(index, distance))
            .OrderByDescending(tuple => tuple.Item2)
            .ToList();

        long[] result = new long[n];
        result[0] = 1;

        int i = 0;
        while (distanceToLastNodeSorted[i].Item1 != 0)
        {
            i++;
        }

        for (int j = i; j < n; j++)
        {
            int node = distanceToLastNodeSorted[j].Item1;
            int distance = distanceToLastNodeSorted[j].Item2;

            foreach (KeyValuePair<int, int> kvp in graph[node])
            {
                int nextNode = kvp.Key;
                int nextDistance = distanceToLastNode[nextNode];

                if (nextDistance < distance)
                {
                    result[nextNode] += result[node];
                    result[nextNode] %= MOD;
                }
            }
        }

        return Convert.ToInt32(result[n - 1]);
    }
}
// @lc code=end

