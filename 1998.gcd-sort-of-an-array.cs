/*
 * @lc app=leetcode id=1998 lang=csharp
 *
 * [1998] GCD Sort of an Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class UnionFindSet {
    private int[] parents;
    public int Count { get; private set; }

    public UnionFindSet(int n) {
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        Count = n;
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
            int pMax = Math.Max(pu, pv);
            int pMin = Math.Min(pu, pv);
            parents[pMax] = pMin;
            Count--;
        }
    }
}

public class Solution {
    private int[] smallestPrimes;

    private int[] SmallestPrimeSieveOfEratosthenes(int n) {
        int[] prime = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            prime[i] = i;
        }

        int p = 2;
        while (p * p <= n) {
            if (prime[p] == p) {
                for (int i = p * p; i <= n; i += p) {
                    if (prime[i] == i) {
                        prime[i] = p;
                    }
                }
            }
            p++;
        }
        return prime;
    }

    private HashSet<int> AllPrimeFactors(int num) {
        HashSet<int> factors = new HashSet<int>();
        if (num <= 1) {
            return factors;
        }

        int p = smallestPrimes[num];
        if (p == num) {
            factors.Add(num);
        } else {
            factors.Add(p);
            factors.UnionWith(AllPrimeFactors(num / p));
        }

        return factors;
    }

    public bool GcdSort(int[] nums) {
        int maxNum = nums.Max();
        int n = nums.Length;

        smallestPrimes = SmallestPrimeSieveOfEratosthenes(maxNum);
        Dictionary<int, List<int>> primeToIndexDict = new Dictionary<int, List<int>>();

        for (int i = 0; i < n; i++) {
            HashSet<int> primes = AllPrimeFactors(nums[i]);
            foreach (int prime in primes) {
                if (!primeToIndexDict.ContainsKey(prime)) {
                    primeToIndexDict[prime] = new List<int>();
                }
                primeToIndexDict[prime].Add(i);
            }
        }

        UnionFindSet uf = new UnionFindSet(n);
        foreach (int p in primeToIndexDict.Keys) {
            for (int i = 1; i < primeToIndexDict[p].Count; i++) {
                uf.Union(primeToIndexDict[p][0], primeToIndexDict[p][i]);
            }
        }

        List<int[]> numSortedWithIndex = new List<int[]>();
        for (int i = 0; i < n; i++) {
            numSortedWithIndex.Add(new int[] { nums[i], i });
        }
        numSortedWithIndex.Sort((a, b) => a[0].CompareTo(b[0]));

        for (int i = 0; i < n; i++) {
            if (uf.Find(numSortedWithIndex[i][1]) != uf.Find(i)) {
                return false;
            }
        }

        return true;
    }
}

// @lc code=end

