/*
 * @lc app=leetcode id=887 lang=csharp
 *
 * [887] Super Egg Drop
 */

// @lc code=start
public class Solution {
    public int SuperEggDrop(int k, int n) {
        int[,] dp = new int[n + 1, k + 1];

        for (int m = 1; m <= n; m++) {
            for (int K = 1; K <= k; K++) {
                dp[m, K] = dp[m - 1, K - 1] + dp[m - 1, K] + 1;
            }

            if (dp[m, k] >= n) {
                return m;
            }
        }

        return -1; // Handle invalid input
    }
}

// @lc code=end

