/*
 * @lc app=leetcode id=1489 lang=csharp
 *
 * [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
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
    public IList<IList<int>> FindCriticalAndPseudoCriticalEdges(int n, int[][] edges) 
    {
        List<int> critical = new List<int>();
        List<int> pseudo = new List<int>();
        UnionFindSet DS = new UnionFindSet(n);
        List<int[]> nonRedundant = new List<int[]>();
        int[] oldParents = new int[n];
        int oldCount = n;

        Dictionary<int, List<int[]>> Weights = new Dictionary<int, List<int[]>>();
        for (int i = 0; i < edges.Length; i++)
        {
            if (!Weights.ContainsKey(edges[i][2]))
            {
                Weights[edges[i][2]] = new List<int[]>();
            }
            Weights[edges[i][2]].Add(new int[3] {edges[i][0], edges[i][1], i});
        }
        int[] weights = Weights.Keys.ToArray();
        Array.Sort(weights);
        foreach (int w in weights)
        {
            nonRedundant.Clear();
            foreach (int[] item in Weights[w])
            {
                if (DS.find(item[0]) != DS.find(item[1]))
                {
                    nonRedundant.Add(item);
                }
            }
            Array.Copy(DS.parents, oldParents, n);
            oldCount = DS.count;
            for (int j = 0; j < nonRedundant.Count; j++)
            {
                for (int k = 0; k < nonRedundant.Count; k++)
                {
                    if (k != j)
                    {
                        DS.union(nonRedundant[k][0], nonRedundant[k][1]);
                    }
                }
                int countPrev = DS.count;
                DS.union(nonRedundant[j][0],nonRedundant[j][1]);
                if (DS.count < countPrev)
                {
                    critical.Add(nonRedundant[j][2]);
                }
                else
                {
                    pseudo.Add(nonRedundant[j][2]);
                }
                Array.Copy(oldParents, DS.parents, n);
                DS.count = oldCount;
            }
            foreach(int[] item in nonRedundant)
            {
                DS.union(item[0], item[1]);
            }
        }
        return new List<IList<int>> {critical, pseudo};
    }
}
// @lc code=end

