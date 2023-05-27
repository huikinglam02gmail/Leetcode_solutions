/*
 * @lc app=leetcode id=1140 lang=csharp
 *
 * [1140] Stone Game II
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    private Dictionary<Tuple<int, int>, int> memo;
    private int[] Piles;
    public int dp(int i, int m)
    {
        Tuple<int, int> t = new Tuple<int, int>(i, m);
        int result = Piles[i];
        if (memo.ContainsKey(t))
        {
            return memo[t];
        }
        else if (i + 2 * m < Piles.Length)
        {
            int optimize = Int32.MaxValue;
            for (int x = 1; x < 2 * m + 1; x++)
            {
                optimize = Math.Min(optimize, dp(i + x, Math.Max(m, x)));
            }
            result -= optimize;
        }
        memo.Add(t, result);
        return result;
    }
    public int StoneGameII(int[] piles) 
    {
        Piles = piles;
        memo = new Dictionary<Tuple<int, int>, int>();
        for (int i = piles.Length - 2; i > -1; i--)
        {
            Piles[i] += Piles[i + 1];
        }
        return dp(0, 1);
    }
}
// @lc code=end

