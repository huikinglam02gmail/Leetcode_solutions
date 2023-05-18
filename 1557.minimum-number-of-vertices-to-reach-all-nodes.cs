/*
 * @lc app=leetcode id=1557 lang=csharp
 *
 * [1557] Minimum Number of Vertices to Reach All Nodes
 */
// @lc code=start

using System.Collections.Generic;
using System.Linq;
public class Solution 
{
    public IList<int> FindSmallestSetOfVertices(int n, IList<IList<int>> edges) 
    {
        HashSet<int> result = Enumerable.Range(0, n).ToHashSet();
        foreach (IList<int> edge in edges)
        {
            if (result.Contains(edge[1]))
            {
                result.Remove(edge[1]);
            }
        }
        return result.ToList();
    }
}
// @lc code=end

