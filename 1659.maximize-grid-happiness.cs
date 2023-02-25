/*
 * @lc app=leetcode id=1659 lang=csharp
 *
 * [1659] Maximize Grid Happiness
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    int M;
    int N;
    Dictionary<Tuple<int, int, int, int, int>, int> cache = new Dictionary<Tuple<int, int, int, int, int>, int>();

    public int dp(int i, int I, int E, int iMask, int eMask)
    {
        Tuple<int, int, int, int, int> t = new Tuple<int, int, int, int, int>(i, I, E, iMask, eMask);
        if (cache.ContainsKey(t))
        {
            return cache[t];
        }
        else
        {
            int result = 0;
            if (i >= 0)
            {
                int[] neigs = new int[2]{0, 0};
                if (((i / N) < (M - 1)) && ((iMask & (1 << (N - 1))) != 0))
                {
                    neigs[0] -= 60;
                    neigs[1] -= 10;
                }
                if (((i / N) < (M - 1)) && ((eMask & (1 << (N - 1))) != 0))
                {
                    neigs[1] += 40;
                    neigs[0] -= 10;
                }
                if (((i % N) < (N - 1)) && ((iMask & 1) != 0))
                {
                    neigs[0] -= 60;
                    neigs[1] -= 10;
                }
                if (((i % N) < (N - 1)) && ((eMask & 1) != 0))
                {
                    neigs[1] += 40;
                    neigs[0] -= 10;
                }

                iMask <<= 1;
                eMask <<= 1;
                if (iMask >= (1 << N))
                {
                    iMask -= (1 << N);
                }
                if (eMask >= (1 << N))
                {
                    eMask -= (1 << N);
                }

                result = dp(i - 1, I, E, iMask, eMask);
                if (I > 0)
                {
                    result = Math.Max(result, 120 + neigs[0] + dp(i - 1, I - 1, E, iMask 
                    + 1, eMask));
                }
                if (E > 0)
                {
                    result = Math.Max(result, 40 + neigs[1] + dp(i - 1, I, E - 1, iMask 
                    , eMask + 1));                    
                }
            }
            cache.Add(t, result);
            return result;
        }
    }

    public int GetMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) 
    {
        M = m;
        N = n;
        return dp(m * n - 1, introvertsCount, extrovertsCount, 0, 0);    
    }
}
// @lc code=end

