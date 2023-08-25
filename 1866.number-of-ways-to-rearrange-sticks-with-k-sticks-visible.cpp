/*
 * @lc app=leetcode id=1866 lang=cpp
 *
 * [1866] Number of Ways to Rearrange Sticks With K Sticks Visible
 */

// @lc code=start
class Solution {
public:
    int rearrangeSticks(int n, int k) {
        vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));
        long long MOD = 1000000007;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                if (j == i) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i - 1][j - 1];
                    dp[i][j] %= MOD;
                    dp[i][j] += (i - 1) * dp[i - 1][j];
                    dp[i][j] %= MOD;
                }
            }
        }
        
        return static_cast<int>(dp[n][k]);
    }
};

// @lc code=end

