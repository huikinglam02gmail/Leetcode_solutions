/*
 * @lc app=leetcode id=1627 lang=csharp
 *
 * [1627] Graph Connectivity With Threshold
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
    public List<int> getPrimes(int n)
    {
        List<int> result = new List<int>();
        if (n >= 2)
        {
            bool[] prime = new bool[n];
            Array.Fill(prime, true);
            prime[0] = false;
            prime[1] = false;
            int i = 2;
            while (i < n)
            {
                if (prime[i])
                {
                    for (long j = i*i; j < n; j+=i)
                    {
                        prime[j] = false;
                    }
                    result.Add(i);
                }
                i++;
            }
        }
        return result;
    }

    public IList<bool> AreConnected(int n, int threshold, int[][] queries) 
    {
        List<int> Primes = getPrimes(n + 1);
        UnionFindSet UF = new UnionFindSet(n + 1);
        for (int i = threshold + 1; i < n + 1; i++)
        {
            int j  = 0;
            while (j < Primes.Count && Primes[j] * i <= n)
            {
                UF.union(i, i * Primes[j]);
                j++;
            }
        }

        List<bool> result = new List<bool>();
        foreach (int[] query in queries)
        {
            result.Add(UF.find(query[0]) == UF.find(query[1]));
        }
        return result;
    }
}
// @lc code=end

