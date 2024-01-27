/*
 * @lc app=leetcode id=629 lang=csharp
 *
 * [629] K Inverse Pairs Array
 */

// @lc code=start
public class Solution {
    public int KInversePairs(int n, int k) {
        const long MOD = 1000000007;
        long[][] dp = new long[n + 1][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new long[k + 1];
            dp[i][0] = 1;
        }

        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                dp[i][j] += dp[i - 1][j];
                dp[i][j] %= MOD;
                dp[i][j] += dp[i][j - 1];
                dp[i][j] %= MOD;
                if (j >= i) {
                    while (dp[i][j] < dp[i - 1][j - 1] + MOD) dp[i][j] += MOD;
                    dp[i][j] -= dp[i - 1][j - i];
                    dp[i][j] %= MOD;
                }                
            }
        }

        return Convert.ToInt32(dp[n][k]);
    }
}

// @lc code=end

