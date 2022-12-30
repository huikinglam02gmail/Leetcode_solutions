/*
 * @lc app=leetcode id=797 lang=csharp
 *
 * [797] All Paths From Source to Target
 */

// @lc code=start
public class Solution 
{
    int[][] Graph;
    List<IList<int>> result;
    public void dfs(List<int> path, int goal, int curr)
    {
        List<int> path1 = new List<int>(path);
        path1.Add(curr);
        if (curr == goal)
        {
            result.Add(path1);
        }
        else
        {
            foreach (int node in Graph[curr])
            {
                dfs(path1, goal, node);
            }
        }
    }
    public IList<IList<int>> AllPathsSourceTarget(int[][] graph) 
    {
        int n = graph.Length;
        Graph = graph;
        result = new List<IList<int>>();
        dfs(new List<int>(), n - 1, 0);
        return result;
    }
}
// @lc code=end

