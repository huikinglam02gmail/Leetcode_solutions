/*
 * @lc app=leetcode id=2642 lang=csharp
 *
 * [2642] Design Graph With Shortest Path Calculator
 */

// @lc code=start
public class Graph {

    private Dictionary<int, int>[] graph;
    public Graph(int n, int[][] edges) {
        graph = new Dictionary<int, int>[n];
        graph = graph.Select(x => new Dictionary<int, int>()).ToArray();
        foreach (int[] edge in edges) graph[edge[0]].Add(edge[1], edge[2]);
    }
    
    public void AddEdge(int[] edge) {
        graph[edge[0]].Add(edge[1], edge[2]);
    }
    
    public int ShortestPath(int node1, int node2) {
        return Dijkstra(node1)[node2];
    }

    private int[] Dijkstra(int source)
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
    
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = new Graph(n, edges);
 * obj.AddEdge(edge);
 * int param_2 = obj.ShortestPath(node1,node2);
 */
// @lc code=end

