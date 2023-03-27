/*
 * @lc app=leetcode id=1697 lang=csharp
 *
 * [1697] Checking Existence of Edge Length Limited Paths
 */

// @lc code=start
using System.Linq;
using System.Collections.Generic;
using System;
public class UnionFindSet
{
    public int[] parents{get; set;}
    public int count{get; set;} 
    public UnionFindSet(int n = 0)
    {
        parents = Enumerable.Range(0, n).ToArray();
        count = n;
    }

    public int find(int u)
    {
        if (u != parents[u])
        {
            parents[u] = find(parents[u]);
        }
        return parents[u];
    }

    public void union(int u, int v)
    {
        int pu = find(u);
        int pv = find(v);
        if (pu != pv)
        {
            int pMax = Math.Max(pu, pv);
            int pMin = Math.Min(pu, pv);
            parents[pMax] = pMin;
            count--;
        }
    }
}
public class Solution 
{
    public bool[] DistanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) 
    {
        queries = queries.Select((v, i) => new int[4]{v[2], v[0], v[1], i}).OrderBy(x => x[0]).ToArray();
        edgeList = edgeList.OrderBy(x => x[2]).ToArray();

        UnionFindSet UF = new UnionFindSet(n);
        int i = 0;
        int j = 0;
        int m = queries.Length;
        int p = edgeList.Length;
        List<Tuple<bool, int>> result = new List<Tuple<bool, int>>();
        while (i < m)
        {
            if (j < p && queries[i][0] > edgeList[j][2])
            {
                UF.union(edgeList[j][0], edgeList[j][1]);
                j++;                
            }
            else if ((j < p && queries[i][0] <= edgeList[j][2]) || j >= p)
            {
                result.Add(new Tuple<bool, int>(UF.find(queries[i][1]) == UF.find(queries[i][2]), queries[i][3]));
                i++;
            }
        }
        return result.OrderBy(x => x.Item2).Select(x => x.Item1).ToArray();
    }
}
// @lc code=end

