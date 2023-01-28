/*
 * @lc app=leetcode id=787 lang=csharp
 *
 * [787] Cheapest Flights Within K Stops
 */

// @lc code=start
public class Solution 
{
    public int FindCheapestPrice(int n, int[][] flights, int src, int dst, int k) 
    {
        Dictionary<int, int>[] graph = new Dictionary<int, int>[n];
        int[] visited = new int[n];
        PriorityQueue<int[], int> queue = new PriorityQueue<int[], int>();
        for (int i = 0; i < n; i++)
        {
            graph[i] = new Dictionary<int, int>();
        }
        foreach (int[] flight in flights)
        {
            graph[flight[0]].Add(flight[1], flight[2]);
        }
        Array.Fill(visited, Int32.MaxValue);

        queue.Enqueue(new int[2]{src, 0}, 0);
        while (queue.TryDequeue(out int[] node, out int price))
        {
            if (node[0] == dst)
            {
                return price;
            }
            if (node[1] < k + 1)
            {
                visited[node[0]] = node[1];
                foreach (int neig in graph[node[0]].Keys)
                {
                    if (node[1] + 1 < visited[neig])
                    {
                        queue.Enqueue(new int[2]{neig, node[1] + 1}, price+ graph[node[0]][neig]); 
                    }
                }
            }
        }
        return -1;
    }
}
// @lc code=end

