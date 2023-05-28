/*
 * @lc app=leetcode id=1547 lang=csharp
 *
 * [1547] Minimum Cost to Cut a Stick
 */

// @lc code=start
using System;
using System.Collections.Generic;
public class Solution 
{
    int[] Cuts;
    Dictionary<Tuple<int, int>, int> memo = new Dictionary<Tuple<int, int>, int>();

    public int MinCost(int n, int[] cuts) 
    {
        Cuts = new int[2 + cuts.Length];
        Cuts[0] = 0;
        Cuts[Cuts.Length - 1] = n;
        Array.Sort(cuts);
        for (int i = 0; i < cuts.Length; i++)
        {
            Cuts[i + 1] = cuts[i];
        }
        return dp(0, Cuts.Length - 1);
    }

    public int dp(int i, int j)
    {
        if (i == j - 1)
        {
            return 0;
        }
        Tuple<int, int> t = new Tuple<int, int> (i, j);
        if (memo.ContainsKey(t))
        {
            return memo[t];
        }
        else
        {
            int cost = Int32.MaxValue;
            for (int k = i + 1; k < j; k++)
            {
                cost = Math.Min(cost, dp(i, k) + dp(k, j));
            }
            int result = Cuts[j] - Cuts[i] + cost;
            memo.Add(t, result);
            return result;
        }
    }
}
// @lc code=end

