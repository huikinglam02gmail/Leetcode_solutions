/*
 * @lc app=leetcode id=1269 lang=csharp
 *
 * [1269] Number of Ways to Stay in the Same Place After Some Steps
 */

// @lc code=start
/**
 * @lc app=leetcode id=1269 lang=csharp
 *
 * [1269] Number of Ways to Stay in the Same Place After Some Steps
 */

public class Solution {
    public int NumWays(int steps, int arrLen) {
        int finalLength = Math.Min(steps, arrLen);
        long MOD = 1000000007;

        long[] dp = new long[finalLength];
        dp[0] = 1;

        for (int i = 0; i < steps; i++) {
            long[] dpNew = new long[finalLength];

            for (int j = 0; j < finalLength; j++) {
                dpNew[j] += dp[j];
                dpNew[j] %= MOD;

                if (j < finalLength - 1) {
                    dpNew[j + 1] += dp[j];
                    dpNew[j + 1] %= MOD;
                }

                if (j > 0) {
                    dpNew[j - 1] += dp[j];
                    dpNew[j - 1] %= MOD;
                }
            }

            dp = dpNew;
        }

        return Convert.ToInt32(dp[0] % MOD);
    }
}

// @lc code=end

