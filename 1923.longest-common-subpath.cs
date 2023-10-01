/*
 * @lc app=leetcode id=1923 lang=csharp
 *
 * [1923] Longest Common Subpath
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int LongestCommonSubpath(int n, int[][] ps)
    {
        ps = ps.OrderBy(x => x.Length).ToArray();
        int l = 1;
        int r = ps[0].Length + 1;
        long baseValue = 100001;
        long mod = 100000000019;

        while (l < r)
        {
            int m = l + (r - l) / 2;
            HashSet<long> hs = new HashSet<long>();

            for (int i = 0; i < ps.Length && (i == 0 || hs.Count > 0); i++)
            {
                long hash = 0;
                long d = 1;
                HashSet<long> hs1 = new HashSet<long>();

                for (int j = 0; j < ps[i].Length; j++)
                {
                    hash = (hash * baseValue + ps[i][j]) % mod;

                    if (j >= m)
                        hash = (mod + hash - d * ps[i][j - m] % mod) % mod;
                    else
                        d = d * baseValue % mod;

                    if (j >= m - 1 && (i == 0 || hs.Contains(hash)))
                        hs1.Add(hash);
                }

                hs = hs1;
            }

            if (hs.Count == 0)
                r = m;
            else
                l = m + 1;
        }

        return l - 1;
    }
}

// @lc code=end

