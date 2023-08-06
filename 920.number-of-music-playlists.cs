/*
 * @lc app=leetcode id=920 lang=csharp
 *
 * [920] Number of Music Playlists
 */

// @lc code=start
public class Solution {
    public int NumMusicPlaylists(int n, int goal, int k) {
        long MOD = 1000000007;
        long[,] dp = new long[goal + 1, n + 1];
        dp[0, 0] = 1;
        
        for (int j = 1; j <= n; j++) {
            for (int i = j; i <= goal; i++) {
                if (i > 0 && j > 0) {
                    dp[i, j] += dp[i - 1, j - 1] * (n - j + 1);
                    dp[i, j] %= MOD;
                }
                if (i > 0) {
                    dp[i, j] += dp[i - 1, j] * Math.Max(j - k, 0);
                    dp[i, j] %= MOD;
                }
            }
        }
        
        return Convert.ToInt32(dp[goal, n]);
    }
}

// @lc code=end

