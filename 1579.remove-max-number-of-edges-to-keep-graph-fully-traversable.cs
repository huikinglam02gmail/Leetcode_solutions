/*
 * @lc app=leetcode id=1579 lang=csharp
 *
 * [1579] Remove Max Number of Edges to Keep Graph Fully Traversable
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
    UnionFindSet DSU;
    public HashSet<int> buildGraph(HashSet<int> canToss, List<List<int>> edges)
    {
        int edgeCount = edges.Count;
        int ind = 0;
        while (ind < edgeCount && DSU.count > 1)
        {
            if (DSU.find(edges[ind][1]) == DSU.find(edges[ind][2]))
            {
                canToss.Add(edges[ind][0]);
            }
            else
            {
                DSU.union(edges[ind][1], edges[ind][2]);
            }
            ind++;
        }
        while (ind < edgeCount)
        {
            canToss.Add(edges[ind][0]);
            ind++;
        }
        return canToss;
    }
    public int MaxNumEdgesToRemove(int n, int[][] edges) 
    {
        int l = edges.Length;
        int[] defaultParents = new int[n];
        int defaultCount = 0;
        List<List<int>> common = new List<List<int>>();
        List<List<int>> Alice = new List<List<int>>();
        List<List<int>> Bob = new List<List<int>>();
        HashSet<int> canToss = new HashSet<int>();
        DSU = new UnionFindSet(n);

        for (int i = 0; i < l; i++)
        {
            if (edges[i][0] == 1)
            {
                Alice.Add(new List<int>() {i, edges[i][1] - 1, edges[i][2] - 1});
            }
            else if (edges[i][0] == 2)
            {
                Bob.Add(new List<int>() {i, edges[i][1] - 1, edges[i][2] - 1});
            }
            else
            {
                common.Add(new List<int>() {i, edges[i][1] - 1, edges[i][2] - 1});
            }
        }
        canToss = buildGraph(canToss, common);

        for (int player = 0; player < 2; player++)
        {
            if (player == 0)
            {
                Array.Copy(DSU.parents, defaultParents, n);
                defaultCount = DSU.count;
                canToss = buildGraph(canToss, Alice);
            }
            else
            {
                Array.Copy(defaultParents, DSU.parents, n);
                DSU.count = defaultCount;
                canToss = buildGraph(canToss, Bob);
            }
            if (DSU.count > 1)
            {
                return -1;
            }
        }
        return canToss.Count;
    }
}
// @lc code=end

