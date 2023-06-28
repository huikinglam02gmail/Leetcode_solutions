/*
 * @lc app=leetcode id=1782 lang=csharp
 *
 * [1782] Count Pairs Of Nodes
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int[] CountPairs(int n, int[][] edges, int[] queries)
    {
        int[] count = new int[n];
        Dictionary<(int, int), int> edgeCount = new Dictionary<(int, int), int>();
        foreach (var edge in edges)
        {
            int a = edge[0], b = edge[1];
            count[a - 1]++;
            count[b - 1]++;
            var pair = (Math.Min(a - 1, b - 1), Math.Max(a - 1, b - 1));
            edgeCount[pair] = edgeCount.GetValueOrDefault(pair, 0) + 1;
        }

        int[] sortedCount = count.OrderBy(x => x).ToArray();
        List<int> result = new List<int>();
        foreach (int q in queries)
        {
            int l = 0, r = n - 1;
            int res = 0;
            while (l < r)
            {
                if (sortedCount[l] + sortedCount[r] <= q)
                    l++;
                else
                {
                    res += r - l;
                    r--;
                }
            }

            foreach (var pair in edgeCount)
            {
                int t = pair.Key.Item1, b = pair.Value;
                if (count[t] + count[pair.Key.Item2] > q && count[t] + count[pair.Key.Item2] - b <= q)
                    res--;
            }
            result.Add(res);
        }
        return result.ToArray();
    }
}

// @lc code=end

