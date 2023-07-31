/*
 * @lc app=leetcode id=712 lang=csharp
 *
 * [712] Minimum ASCII Delete Sum for Two Strings
 */

// @lc code=start
public class Solution {
    /*
     * Classic DP string comparison problem
     * Build a 2D dp between the strings, with an extra position for the empty character
     * dp[i][j] = the lowest ASCII sum of deleted characters to make s1[:j] and s2[:i] equal.
     * The recursion formula is simple:
     * if s1[i] == s2[j]: dp[i][j] = dp[i-1][j-1]
     * else: dp[i][j] = Math.Min((int)s2[i] + dp[i-1][j], (int)s1[j] + dp[i][j-1])
     */
    public int MinimumDeleteSum(string s1, string s2) {
        int m = s2.Length;
        int n = s1.Length;
        int[,] dp = new int[m + 1, n + 1];
        for (int i = 0; i < m + 1; i++)
        {
            for (int j = 0; j < n + 1; j++)
            {
                dp[i, j] = Int32.MaxValue;
            }
        }

        dp[0, 0] = 0;
        for (int i = 1; i <= n; i++)
            dp[0, i] = dp[0, i - 1] + (int)s1[i - 1];

        for (int i = 1; i <= m; i++)
            dp[i, 0] = dp[i - 1, 0] + (int)s2[i - 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i, j] = Math.Min(dp[i, j], dp[i - 1, j] + (int)s2[i - 1]);
                dp[i, j] = Math.Min(dp[i, j], dp[i, j - 1] + (int)s1[j - 1]);

                if (s2[i - 1] == s1[j - 1])
                    dp[i, j] = Math.Min(dp[i, j], dp[i - 1, j - 1]);
            }
        }

        return dp[m, n];
    }
}

// @lc code=end

