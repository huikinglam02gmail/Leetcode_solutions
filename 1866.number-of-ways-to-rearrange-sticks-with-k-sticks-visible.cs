/*
 * @lc app=leetcode id=1866 lang=csharp
 *
 * [1866] Number of Ways to Rearrange Sticks With K Sticks Visible
 */

// @lc code=start
public class Solution {
    public int RearrangeSticks(int n, int k) {
        long[,] dp = new long[n + 1, n + 1];
        long MOD = 1000000007;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                if (j == i) {
                    dp[i, j] = 1;
                } else {
                    dp[i, j] = dp[i - 1, j - 1];
                    dp[i, j] %= MOD;
                    dp[i, j] += (i - 1) * dp[i - 1, j];
                    dp[i, j] %= MOD;
                }
            }
        }
        
        return Convert.ToInt32(dp[n, k]);
    }
}

// @lc code=end

