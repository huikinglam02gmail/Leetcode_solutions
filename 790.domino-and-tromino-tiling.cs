/*
 * @lc app=leetcode id=790 lang=csharp
 *
 * [790] Domino and Tromino Tiling
 */

// @lc code=start
public class Solution 
{
    public int NumTilings(int n) 
    {
        long MOD = 1000000007;
        long[] dp = new long[Math.Max(4, n + 3)];
        long result = 1;
        Array.Fill(dp, 0);
        for (int i = 0; i < 4; i++)
        {
            if (i > 1)
            {
                dp[i] = 1;
            }
        }   
        for (int i = 4; i < n + 3; i++)
        {
            if (i > 4)
            {
                result -= dp[i - 5];
                result += MOD;
                result %= MOD;
            }
            result += dp[i - 1];
            result %= MOD;
            dp[i] = dp[i - 2] + result;
            dp[i] %= MOD;
        }
        return Convert.ToInt32(result);
    }
}
// @lc code=end
