/*
 * @lc app=leetcode id=1519 lang=csharp
 *
 * [1519] Number of Nodes in the Sub-Tree With the Same Label
 */

// @lc code=start
public class Solution 
{
    public int[] CountSubTrees(int n, int[][] edges, string labels) 
    {
        HashSet<int>[] graph = new HashSet<int>[n];
        Queue<int> queue = new Queue<int>();
        int[] parents = new int[n];
        int[] adjacency = new int[n];
        int[][] counts = new int[n][];
        int[] result = new int[n];

        Array.Fill(result, 0);
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
            counts[i] = new int[26];
            Array.Fill(counts[i], 0);
        }
        foreach (int[] edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }

        queue.Enqueue(0);
        Array.Fill(parents, -2);
        Array.Fill(adjacency, 0);
        parents[0] = -1;
        while (queue.TryDequeue(out int node))
        {
            foreach (int nxt in graph[node])
            {
                if (parents[nxt] == -2)
                {
                    queue.Enqueue(nxt);
                    parents[nxt] = node;
                    adjacency[node]++;
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            if (adjacency[i] == 0)
            {
                queue.Enqueue(i);
            }
        }

        while (queue.TryDequeue(out int node))
        {
            counts[node][(int) labels[node] - (int) 'a']++;
            result[node] = counts[node][(int) labels[node] - (int) 'a'];
            if (parents[node] >= 0)
            {
                for (int j = 0; j < 26; j++)
                {
                    counts[parents[node]][j] += counts[node][j];
                }
                adjacency[parents[node]]--;
                if (adjacency[parents[node]] == 0)
                {
                    queue.Enqueue(parents[node]);
                }
            }
        }
        return result;
    }
}
// @lc code=end

