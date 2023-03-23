/*
 * @lc app=leetcode id=1319 lang=csharp
 *
 * [1319] Number of Operations to Make Network Connected
 */

// @lc code=start
public class Solution 
{
    public int MakeConnected(int n, int[][] connections) 
    {
        if (connections.Length < n - 1)
        {
            return -1;
        }
        HashSet<int>[] graph = new HashSet<int>[n];
        graph = graph.Select(x => new HashSet<int>()).ToArray();
        bool[] visited = new bool[n];
        Queue<int> queue = new Queue<int>();        
        foreach (int[] connection in connections)
        {
            graph[connection[0]].Add(connection[1]);
            graph[connection[1]].Add(connection[0]);
        }
        Array.Fill(visited, false);

        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                queue.Enqueue(i);
                visited[i] = true;
                count++;
                while (queue.TryDequeue(out int node))
                {
                    foreach (int nxt in graph[node])
                    {
                        if (!visited[nxt])
                        {
                            queue.Enqueue(nxt);
                            visited[nxt] = true;
                        }
                    }
                }
            }
        }
        return count - 1;
    }
}
// @lc code=end

