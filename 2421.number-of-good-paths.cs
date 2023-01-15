/*
 * @lc app=leetcode id=2421 lang=csharp
 *
 * [2421] Number of Good Paths
 */

// @lc code=start
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
    int[][] maxValues;
    public int maxValueCount(int node, int value)
    {
        if (value == maxValues[node][0])
        {
            return maxValues[node][1];
        }
        else
        {
            return 0;
        }
    }
    public int NumberOfGoodPaths(int[] vals, int[][] edges) 
    {
        int n = vals.Length;
        int result = n;
        UnionFindSet UF = new UnionFindSet(n);
        maxValues = new int[n][];
        for (int i = 0; i < n; i++)
        {
            maxValues[i] = new int[2]{vals[i], 1};
        }
        List<int[]> data = new List<int[]>();
        foreach (int[] edge in edges)
        {
            int maxVal = Math.Max(vals[edge[0]], vals[edge[1]]);
            int nodeMax = Math.Max(edge[0], edge[1]);
            int nodeMin = Math.Min(edge[0], edge[1]);
            data.Add(new int[3]{maxVal, nodeMin, nodeMax});
        }
        data = data.OrderBy(x => x[0]).ThenBy(x => x[1]).ThenBy(x => x[2]).ToList();

        foreach (int[] datum in data)
        {
            int node1p = UF.find(datum[1]);
            int node2p = UF.find(datum[2]);
            int maxValueCount1 = maxValueCount(node1p, datum[0]);
            int maxValueCount2 = maxValueCount(node2p, datum[0]);
            result += maxValueCount1 * maxValueCount2;
            UF.union(node1p, node2p);
            maxValues[node1p] = new int[2]{datum[0], maxValueCount1 + maxValueCount2};
        }

        return result;
    }
}
// @lc code=end

