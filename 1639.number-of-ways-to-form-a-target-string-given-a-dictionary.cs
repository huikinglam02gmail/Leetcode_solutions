/*
 * @lc app=leetcode id=1639 lang=csharp
 *
 * [1639] Number of Ways to Form a Target String Given a Dictionary
 */

// @lc code=start
public class Solution 
{
    public int NumWays(string[] words, string target) 
    {
        long MOD = 1000000007;
        int m = words[0].Length;
        int n = target.Length;
        long[] dp = new long[n + 1];
        Array.Fill(dp, 0);
        dp[0] = 1;
        for (int i = 0; i < m; i++)
        {
            int[] seen = new int[26];
            Array.Fill(seen, 0);
            foreach (string word in words)
            {
                seen[(int) word[i] - (int) 'a']++;
            } 
            for (int j = n - 1; j >= 0; j--)
            {
                dp[j + 1] += dp[j] * seen[(int) target[j] - (int) 'a'];
                dp[j + 1] %= MOD;
            }
        }   
        return Convert.ToInt32(dp[n]);
    }
}
// @lc code=end

