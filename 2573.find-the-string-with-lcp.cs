/*
 * @lc app=leetcode id=2573 lang=csharp
 *
 * [2573] Find the String with LCP
 */

// @lc code=start
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
    public string FindTheString(int[][] lcp) 
    {
        int n = lcp.Length;
        UnionFindSet UF = new UnionFindSet(n);
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                if (lcp[i][j] != lcp[j][i] || lcp[i][j] > n - j || (i >= 1 && j >= 1 && lcp[i - 1][j - 1] > 0 && lcp[i][j] != lcp[i - 1][j - 1] - 1))
                {
                    return "";
                }
                if (lcp[i][j] > 0)
                {
                    UF.union(i, j);
                }
            }
        }    

        if (UF.count > 26)
        {
            return "";
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                if ((lcp[i][j] == 0 && UF.find(i) == UF.find(j)) || (lcp[i][j] > 0 && UF.find(i) != UF.find(j)))
                {
                    return "";
                }
            }
        }

        string[] result = new string[n];
        Array.Fill(result, string.Empty);
        Dictionary<int, List<int>> parents = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++)
        {
            int parent = UF.find(i);
            if (!parents.ContainsKey(parent))
            {
                parents[parent] = new List<int>();
            }
            parents[parent].Add(i);
        }

        string alphabets = "abcdefghijklmnopqrstuvwxyz";
        int l = 0;
        for (int i = 0; i < n; i++)
        {
            if (result[i].Equals(string.Empty))
            {
                foreach (int k in parents[UF.find(i)])
                {
                    result[k] = alphabets[l].ToString();
                }
                l++;
            }
        }
        return string.Join(string.Empty, result);
    }
}
// @lc code=end
