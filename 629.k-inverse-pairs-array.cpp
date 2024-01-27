/*
 * @lc app=leetcode id=629 lang=cpp
 *
 * [629] K Inverse Pairs Array
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int kInversePairs(int n, int k) {
        const long MOD = 1000000007;
        std::vector<std::vector<long>> dp(n + 1, std::vector<long>(k + 1, 0));

        for (int i = 0; i <= n; i++) {
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

        return static_cast<int>(dp[n][k]);
    }
};

// @lc code=end

