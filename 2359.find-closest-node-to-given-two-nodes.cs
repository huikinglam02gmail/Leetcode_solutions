/*
 * @lc app=leetcode id=2359 lang=csharp
 *
 * [2359] Find Closest Node to Given Two Nodes
 */

// @lc code=start
public class Solution 
{
    HashSet<int>[] graph;
    public int[] bfs(int startNode, int[] distanceArray)
    {
        Queue<int> queue = new Queue<int>();
        HashSet<int> visited = new HashSet<int>();
        int steps = 0;
        queue.Enqueue(startNode);
        visited.Add(startNode);
        while (queue.Count > 0)
        {
            int n = queue.Count;
            for (int i = 0; i < n; i++)
            {
                int node = queue.Dequeue();
                distanceArray[node] = Math.Min(distanceArray[node], steps);
                foreach (int nxt in graph[node])
                {
                    if (!visited.Contains(nxt))
                    {
                        visited.Add(nxt);
                        queue.Enqueue(nxt);
                    }
                }
            }
            steps++;
        }
            
        return distanceArray;    
    }

    public int ClosestMeetingNode(int[] edges, int node1, int node2) 
    {
        int n = edges.Length;
        int minSoFar = n;
        int minIndex = -1;
        graph = new HashSet<int>[n];
        int[] dist1 = new int[n];
        int[] dist2 = new int[n];
        Array.Fill(dist1, n);
        Array.Fill(dist2, n);
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
            if (edges[i] != -1)
            {
                graph[i].Add(edges[i]);
            }
        }

        dist1 = bfs(node1, dist1);
        dist2 = bfs(node2, dist2);

        for (int i = 0; i < n; i++)
        {
            if (Math.Max(dist1[i], dist2[i]) < minSoFar)
            {
                minIndex = i;
                minSoFar = Math.Max(dist1[i], dist2[i]);
            }
        }
        return minIndex;
    }
}
// @lc code=end

