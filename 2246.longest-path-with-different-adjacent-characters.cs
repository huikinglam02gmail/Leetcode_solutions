/*
 * @lc app=leetcode id=2246 lang=csharp
 *
 * [2246] Longest Path With Different Adjacent Characters
 */

// @lc code=start
public class Solution 
{
    string S;
    int result;
    HashSet<int>[] graph;

    public int dfs(int node)
    {
        int[] nodeTopTwo = new int[2]{1, 1};
        foreach (int i in graph[node])
        {
            int childrenMaxPathLength = dfs(i);
            if (S[i] != S[node])
            {
                int newComer = 1 + childrenMaxPathLength;
                for (int j = 0; j < 2; j++)
                {
                    if (newComer > nodeTopTwo[j])
                    {
                        int temp = newComer;
                        newComer = nodeTopTwo[j];
                        nodeTopTwo[j] = temp;
                    }
                }
            }
        }
        result = Math.Max(result, nodeTopTwo[0] + nodeTopTwo[1] - 1);
        return nodeTopTwo[0];
    }

    public int LongestPath(int[] parent, string s) 
    {
        int n = parent.Length;
        graph = new HashSet<int>[n];
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }

        S = s;
        result = 0;
        for (int i = 0; i < n; i++)
        {
            if (parent[i] >= 0)
            {
                graph[parent[i]].Add(i);
            }
        }
        int rootMaxPathLength = dfs(0);
        return result;
    }
}
// @lc code=end
