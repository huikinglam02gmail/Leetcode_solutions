/*
 * @lc app=leetcode id=1916 lang=csharp
 *
 * [1916] Count Ways to Build Rooms in an Ant Colony
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    private const int MOD = 1000000007;
    private long[] fac;
    private long[] ifac;

    public int WaysToBuildRooms(int[] prevRoom)
    {
        int n = prevRoom.Length;

        // Construct tree.
        List<List<int>> g = new List<List<int>>();
        for (int i = 0; i < n; i++)
        {
            g.Add(new List<int>());
        }
        for (int i = 1; i < n; ++i)
        {
            g[prevRoom[i]].Add(i);
        }

        // Pre-process fac and inv fac.
        fac = new long[n + 1];
        ifac = new long[n + 1];
        fac[0] = 1;
        ifac[0] = 1;
        for (int i = 1; i <= n; ++i)
        {
            fac[i] = fac[i - 1] * i % MOD;
            ifac[i] = QPow(fac[i], MOD - 2);
        }

        return Convert.ToInt32(DFS(g, fac, ifac, 0).Item1);
    }

    private long QPow(long x, long n)
    {
        long ans = 1;
        while (n > 0)
        {
            if (n % 2 == 1)
            {
                ans *= x;
                ans %= MOD;
            }

            x *= x;
            x %= MOD;
            n /= 2;
        }
        return ans;
    }

    private Tuple<long, long> DFS(List<List<int>> g, long[] fac, long[] ifac, int cur)
    {
        if (g[cur].Count == 0)
        {
            return new Tuple<long, long>(1, 1);
        }
        long ans = 1;
        long l = 0;
        foreach (int nxt in g[cur])
        {
            Tuple<long, long> temp = DFS(g, fac, ifac, nxt);
            long tmp = temp.Item1;
            long r = temp.Item2;
            long comb = fac[l + r];
            comb *= ifac[l];
            comb %= MOD;
            comb *= ifac[r];
            comb %= MOD;
            ans *= tmp;
            ans %= MOD;
            ans *= comb;
            ans %= MOD;
            l += r;
        }
        return new Tuple<long, long>(ans, l + 1);
    }
}

// @lc code=end

