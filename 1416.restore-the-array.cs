/*
 * @lc app=leetcode id=1416 lang=csharp
 *
 * [1416] Restore The Array
 */

// @lc code=start
using System;
public class Solution 
{
    public int NumberOfArrays(string s, int k) 
    {
        int n = s.Length;
        int l = k.ToString().Length;
        long MOD = 1000000007;
        long[] dp = new long[n + 1];
        Array.Fill(dp, 0);
        dp[n] = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            if (s[i]!='0')
            {
                for (int j = i + 1; j < 1 + Math.Min(n, i + l); j++)
                {
                    string current = s.Substring(i, j - i);
                    if (Int64.Parse(current) >= 1 && Int64.Parse(current) <= k)
                    {
                        dp[i] += dp[j];
                    }
                }
                dp[i] %= MOD;
            }
        }
        return Convert.ToInt32(dp[0]);
    }
}
// @lc code=end

