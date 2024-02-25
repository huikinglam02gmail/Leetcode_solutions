/*
 * @lc app=leetcode id=2709 lang=csharp
 *
 * [2709] Greatest Common Divisor Traversal
 */

// @lc code=start
using System.Collections.Generic;

public class UnionFindSet {
    public int[] parents;
    public int count;

    public UnionFindSet(int n) {
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        count = n;
    }

    public int Find(int u) {
        if (u != parents[u]) {
            parents[u] = Find(parents[u]);
        }
        return parents[u];
    }

    public void Union(int u, int v) {
        int pu = Find(u);
        int pv = Find(v);
        if (pu != pv) {
            int pMax = System.Math.Max(pu, pv);
            int pMin = System.Math.Min(pu, pv);
            parents[pMax] = pMin;
            count--;
        }
    }
}

public class Solution {
    public bool CanTraverseAllPairs(int[] nums) {
        if (nums.Length == 1) return true;
        Dictionary<int, List<int>> primeIndicesDict = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) return false;
            Dictionary<int, int> primeFacs = PrimeFactors(nums[i]);
            foreach (var kvp in primeFacs) {
                int prime = kvp.Key;
                int indices = kvp.Value;
                if (!primeIndicesDict.ContainsKey(prime)) primeIndicesDict[prime] = new List<int>();
                primeIndicesDict[prime].Add(i);
            }
        }
        UnionFindSet uf = new UnionFindSet(nums.Length);
        foreach (var kvp in primeIndicesDict) {
            List<int> indices = kvp.Value;
            for (int i = 1; i < indices.Count; i++) {
                uf.Union(indices[0], indices[i]);
            }
        }
        return uf.count == 1;
    }

    public Dictionary<int, int> PrimeFactors(int n) {
        Dictionary<int, int> primes = new Dictionary<int, int>();
        while (n % 2 == 0) {
            primes[2] = primes.ContainsKey(2) ? primes[2] + 1 : 1;
            n /= 2;
        }

        int i = 3;
        while (i * i <= n) {
            while (n % i == 0) {
                primes[i] = primes.ContainsKey(i) ? primes[i] + 1 : 1;
                n /= i;
            }
            i += 2;
        }
        if (n > 1) {
            primes[n] = primes.ContainsKey(n) ? primes[n] + 1 : 1;
        }
        return primes;
    }
}

// @lc code=end

