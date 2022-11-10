/*
 * @lc app=leetcode id=1443 lang=csharp
 *
 * [1443] Minimum Time to Collect All Apples in a Tree
 */

// @lc code=start
public class Solution 
{
    HashSet<int>[] graph;
    List<bool> Apple;

    public int dfs(int node, int parent)
    {
        int result = 0;
        foreach (int nxt in graph[node])
        {
            if (nxt != parent)
            {
                result += dfs(nxt, node);
            }
        }
        if (Apple[node] || result > 0)
        {
            result += 2;
        }
        return result;
    }

    public int MinTime(int n, int[][] edges, IList<bool> hasApple) 
    {
        graph = new HashSet<int>[n];
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }
        Apple = hasApple.ToList();
        for (int i = 0; i < edges.Length; i++)
        {
            graph[edges[i][0]].Add(edges[i][1]);
            graph[edges[i][1]].Add(edges[i][0]);
        }
        int result = dfs(0, -1);
        if (result > 0)
        {
            result -= 2;
        }
        return result;
    }
}
// @lc code=end

