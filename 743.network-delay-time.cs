/*
 * @lc app=leetcode id=743 lang=csharp
 *
 * [743] Network Delay Time
 */

// @lc code=start
public class Solution 
{
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
            result[node] = weight;
            if (!visited[node])
            {
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
    public int NetworkDelayTime(int[][] times, int n, int k) 
    {
        Dictionary<int, int>[] graph = new Dictionary<int, int>[n];
        graph = graph.Select(x => new Dictionary<int, int>()).ToArray();
        foreach (int[] time in times)
        {
            graph[time[0] - 1].Add(time[1] - 1, time[2]);
        }

        int[] result = Dijkstra(graph, k - 1);
        Array.Sort(result);
        return result[0] == -1 ? -1 : result.Last();
    }
}
// @lc code=end

