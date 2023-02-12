/*
 * @lc app=leetcode id=2477 lang=csharp
 *
 * [2477] Minimum Fuel Cost to Report to the Capital
 */

// @lc code=start
public class Solution 
{
    long result;
    int Seats;
    HashSet<int>[] graph;

    private int dfs(int node, int parent)
    {
        int count = 1;
        foreach (int nxt in graph[node])
        {
            if (nxt != parent)
            {
                int childCount = dfs(nxt, node);
                result += Convert.ToInt64(Math.Ceiling((double) childCount / Seats));
                count += childCount;
            }
        }
        return count;
    }
    public long MinimumFuelCost(int[][] roads, int seats) 
    {
        result = 0;
        Seats = seats;
        int n = roads.Length + 1;
        graph = new HashSet<int>[n];
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }
        foreach (int[] road in roads)
        {
            graph[road[0]].Add(road[1]);
            graph[road[1]].Add(road[0]);
        }

        int total = dfs(0, -1);
        return result;
    }
}
// @lc code=end

