/*
 * @lc app=leetcode id=1719 lang=csharp
 *
 * [1719] Number Of Ways To Reconstruct A Tree
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
public class Solution 
{
    public int CheckWays(int[][] pairs) 
    {
        Dictionary<int, HashSet<int>> graph = new Dictionary<int, HashSet<int>>();
        foreach (int[] pair in pairs)
        {
            if (!graph.ContainsKey(pair[0]))
            {
                graph.Add(pair[0], new HashSet<int>());
            }
            if (!graph.ContainsKey(pair[1]))
            {
                graph.Add(pair[1], new HashSet<int>());
            }
            graph[pair[0]].Add(pair[1]);
            graph[pair[1]].Add(pair[0]);
        }

        HashSet<int> visited = new HashSet<int>();
        bool multiple = false;
        int[] graphKeys = graph.Select(x => x.Key).OrderBy(y => -graph[y].Count).ToArray();
        foreach (int x in graphKeys)
        {
            HashSet<int> parentCandidates = graph[x].Select(x => x).ToHashSet();
            parentCandidates.IntersectWith(visited);
            visited.Add(x);
            if (parentCandidates.Count == 0)
            {
                if (graph[x].Count != graph.Count - 1)
                {
                    return 0;
                }
            }
            else
            {
                int p = parentCandidates.Select(x => x).OrderBy(x => graph[x].Count).First();
                HashSet<int> parentSubset = graph[p].Select(x => x).ToHashSet();
                parentSubset.Add(p);
                if (!graph[x].IsSubsetOf(parentSubset))
                {
                    return 0;
                }
                multiple = multiple || (graph[x].Count == graph[p].Count);
            }
        }
        return 1 + (multiple ? 1 : 0);
    }
}
// @lc code=end

