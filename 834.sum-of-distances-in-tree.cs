/*
 * @lc app=leetcode id=834 lang=csharp
 *
 * [834] Sum of Distances in Tree
 */

// @lc code=start
public class Solution 
{
    HashSet<int>[] graph;
    int[] weight;
    int[] answer;
    int root;

    public int[] dfs(int node, int parent, int depth)
    {
        int count = 1;
        int distance = depth;
        foreach (int child in graph[node])
        {
            if (child != parent)
            {
                int[] resultChild = dfs(child, node, depth + 1);
                count += resultChild[0];
                distance += resultChild[1];
            }
        }
        weight[node] = count;
        return new int[2] {count, distance};
    }

    public void dfs2(int node, int parent, int n)
    {
        foreach (int child in graph[node])
        {
            if (child != parent)
            {
                answer[child] = answer[node] + n - 2*weight[child];
                dfs2(child, node, n);
            }
        }
    }
    public int[] SumOfDistancesInTree(int n, int[][] edges) 
    {
        graph = new HashSet<int>[n];
        weight = new int[n];
        answer = new int[n];
        root = 0;

        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }
        foreach (int[] edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }

        int[] result = dfs(root, -1, 0);
        answer[root] = result[1];
        dfs2(root, -1, n);
        return answer;
    }
}
// @lc code=end

