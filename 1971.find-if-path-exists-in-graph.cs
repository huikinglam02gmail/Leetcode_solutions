/*
 * @lc app=leetcode id=1971 lang=csharp
 *
 * [1971] Find if Path Exists in Graph
 */

// @lc code=start
public class Solution 
{
    public bool ValidPath(int n, int[][] edges, int source, int destination) 
    {
        HashSet<int>[] graph = new HashSet<int>[n];
        Queue<int> queue = new Queue<int>();
        bool[] visited = new bool[n];

        Array.Fill(visited, false);
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }

        foreach (int[] edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }

        queue.Enqueue(source);
        visited[source] = true;
        while (queue.TryDequeue(out int node))
        {
            if (node == destination)
            {
                return true;
            }
            foreach (int nxt in graph[node])
            {
                if (!visited[nxt])
                {
                    visited[nxt] = true;
                    queue.Enqueue(nxt);
                }
            }
        }
        return false;
    }
}
// @lc code=end

