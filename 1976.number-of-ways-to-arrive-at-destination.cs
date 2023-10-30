/*
 * @lc app=leetcode id=1976 lang=csharp
 *
 * [1976] Number of Ways to Arrive at Destination
 */

// @lc code=start
public class Solution {
    Dictionary<int, int>[] graph;
    long[] dp;
    long MOD = 1000000007;
    PriorityQueue<Tuple<int, long>, long> pq;
    public long[] Dijkstra(Dictionary<int, int>[] graph, int source)
    {
        int n = graph.Length;
        long[] result = new long[n];
        Array.Fill(result, -1);

        PriorityQueue<int, long> heap = new PriorityQueue<int, long>();
        bool[] visited = new bool[n];
        Array.Fill(visited, false);
        int visitedCount = 0;
        heap.Enqueue(source, 0);

        while (heap.TryDequeue(out int node, out long weight) && visitedCount < n)
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
    public int CountPaths(int n, int[][] roads) 
    {
        graph = new Dictionary<int, int>[n];
        graph = graph.Select(x => new Dictionary<int, int>()).ToArray();
        foreach (int[] road in roads)
        {
            graph[road[0]].Add(road[1], road[2]);
            graph[road[1]].Add(road[0], road[2]);
        }
        long[] SSP = Dijkstra(graph, 0);

        dp = new long[n];
        pq = new PriorityQueue<Tuple<int, long>, long>();
        pq.Enqueue(new Tuple<int, long>(0, 1), 0);
        int[] nodesInHeap = new int[n];
        nodesInHeap[0]++;

        while (pq.TryDequeue(out Tuple<int, long> t, out long arrivalTime))
        {
            dp[t.Item1] += t.Item2;
            dp[t.Item1] %= MOD;
            nodesInHeap[t.Item1]--;
            if (t.Item1 != n - 1 && nodesInHeap[t.Item1] == 0)
            {
                foreach (KeyValuePair<int,int> kvp in graph[t.Item1])
                {
                    if (Convert.ToInt64(arrivalTime + kvp.Value) == SSP[kvp.Key])
                    {
                        pq.Enqueue(new Tuple<int, long>(kvp.Key, dp[t.Item1]), arrivalTime + kvp.Value);
                        nodesInHeap[kvp.Key]++;
                    }
                }
            }
        }
        return Convert.ToInt32(dp[n - 1]);
    }
}
// @lc code=end

