/*
 * @lc app=leetcode id=1584 lang=csharp
 *
 * [1584] Min Cost to Connect All Points
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
    public int MinCostConnectPoints(int[][] points) 
    {
        int n = points.Length;
        UnionFindSet DSU = new UnionFindSet(n);
        int result = 0;
        PriorityQueue<Tuple<int, int>, int> heap = new PriorityQueue<Tuple<int, int>, int>();
        for (int i = 0; i < n - 1; i++)
        {
            int xi = points[i][0];
            int yi = points[i][1];
            for (int j = i + 1; j < n; j++)
            {
                int xj = points[j][0];
                int yj = points[j][1];
                heap.Enqueue(new Tuple<int,int>(i,j), Math.Abs(xi - xj) + Math.Abs(yi - yj));
            }
        }
        while (DSU.count > 1)
        {
            if (heap.TryDequeue(out Tuple<int, int> t, out int dist) && DSU.find(t.Item1) != DSU.find(t.Item2))
            {
                DSU.union(t.Item1, t.Item2);
                result += dist;
            }
        }
        return result;
    }
}
// @lc code=end

