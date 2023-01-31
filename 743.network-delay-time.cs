/*
 * @lc app=leetcode id=743 lang=csharp
 *
 * [743] Network Delay Time
 */

// @lc code=start
public class Solution 
{
    public int NetworkDelayTime(int[][] times, int n, int k) 
    {
        Dictionary<int, int>[] graph = new Dictionary<int, int>[n];
        PriorityQueue<int, int> queue = new PriorityQueue<int, int>();
        bool[] visited = new bool[n];
        int visitedCount = 0;
        int result = -1;
        
        for (int i = 0; i < n; i++)
        {
            graph[i] = new Dictionary<int, int>();
        }

        foreach (int[] time in times)
        {
            graph[time[0] - 1].Add(time[1] - 1, time[2]);
        }
        Array.Fill(visited, false);
        queue.Enqueue(k - 1, 0);
        while (visitedCount < n && queue.TryDequeue(out int node, out int time))
        {
            result = time;
            if (!visited[node])
            {
                visited[node] = true;
                visitedCount++;
                foreach (int nxt in graph[node].Keys)
                {
                    queue.Enqueue(nxt, time + graph[node][nxt]);
                }
            }
        }

        if (visitedCount < n)
        {
            return -1;
        }
        else
        {
            return result;
        }
    }
}
// @lc code=end

