/*
 * @lc app=leetcode id=2466 lang=csharp
 *
 * [2466] Count Ways To Build Good Strings
 */

// @lc code=start
using System;
public class Solution 
{
    public int CountGoodStrings(int low, int high, int zero, int one) 
    {
        long MOD = 1000000007;
        long[] dp = new long[high + 1];
        Array.Fill(dp, 0);
        dp[zero]++;
        dp[one]++;
        long result = 0;
        for (int i = Math.Min(zero, one); i< high + 1; i++)
        {
            if (i + zero < high + 1)
            {
                dp[i + zero] += dp[i];
                dp[i + zero] %= MOD;
            }
            if (i + one < high + 1)
            {
                dp[i + one] += dp[i];
                dp[i + one] %= MOD;
            }
            if (low <= i && i <= high)
            {
                result += dp[i];
                result %= MOD;
            }
        }
        return Convert.ToInt32(result);
    }
}
// @lc code=end

