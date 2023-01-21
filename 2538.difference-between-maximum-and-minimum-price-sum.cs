/*
 * @lc app=leetcode id=2538 lang=csharp
 *
 * [2538] Difference Between Maximum and Minimum Price Sum
 */

// @lc code=start
public class Solution 
{
    HashSet<int>[] graph;
    long[] subTreeSum;
    int[] Price;
    long result;
    public long dfs(int node, int parent)
    {
        long m = 0;
        foreach (int nxt in graph[node])
        {
            if (nxt != parent)
            {
                m = Math.Max(m, dfs(nxt, node));
            }
        }
        subTreeSum[node] = m + Price[node];
        return subTreeSum[node];
    }
    public void dfs2(int node, int parent, long parentContribution)
    {
        int maxChild = -1;
        long largestChildContribution = 0;
        long secondChildContribution = 0;
        foreach (int nxt in graph[node])
        {
            if (nxt == parent)
            {
                continue;
            }
            else if(subTreeSum[nxt] > largestChildContribution)
            {
                secondChildContribution = largestChildContribution;
                largestChildContribution = subTreeSum[nxt];
                maxChild = nxt;
            }
            else if (subTreeSum[nxt] > secondChildContribution)
            {
                secondChildContribution = subTreeSum[nxt];
            }
        }
        result = Math.Max(result, largestChildContribution);
        result = Math.Max(result, parentContribution);

        foreach (int nxt in graph[node])
        {
            if (nxt == parent)
            {
                continue;
            }
            else if (nxt == maxChild)
            {
                dfs2(nxt, node, Price[node] + Math.Max(parentContribution, secondChildContribution));
            }
            else
            {
                dfs2(nxt, node, Price[node] + Math.Max(parentContribution, largestChildContribution));
            }
        }
    }

    public long MaxOutput(int n, int[][] edges, int[] price) 
    {
        graph = new HashSet<int>[n];
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }    
        foreach (int[] edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }
        Price = price;
        result = 0;
        subTreeSum = new long[n];
        Array.Fill(subTreeSum, 0);
        dfs(0, -1);
        dfs2(0, -1, 0);
        return result;
    }
}
// @lc code=end

