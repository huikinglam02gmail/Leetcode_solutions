/*
 * @lc app=leetcode id=1884 lang=csharp
 *
 * [1884] Egg Drop With 2 Eggs and N Floors
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

    public int TwoEggDrop(int n) {
        return SuperEggDrop(2, n);
    }
}

// @lc code=end

