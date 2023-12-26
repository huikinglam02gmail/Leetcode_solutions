/*
 * @lc app=leetcode id=1155 lang=csharp
 *
 * [1155] Number of Dice Rolls With Target Sum
 */

// @lc code=start
public class Solution {
    public int NumRollsToTarget(int n, int k, int target) {
        int MOD = (int)Math.Pow(10, 9) + 7;
        int[][] dp = new int[n][];
        
        for (int i = 0; i < n; i++) {
            dp[i] = new int[target + 1];
        }
        
        for (int j = 1; j <= Math.Min(k, target); j++) {
            dp[0][j] += 1;
        }
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j <= target; j++) {
                for (int l = 1; l <= k; l++) {
                    if (j + l < target + 1) {
                        dp[i + 1][j + l] = (dp[i + 1][j + l] + dp[i][j]) % MOD;
                    }
                }
            }
        }
        
        return dp[n - 1][target];
    }
}

// @lc code=end

