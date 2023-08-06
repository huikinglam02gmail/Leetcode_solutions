/*
 * @lc app=leetcode id=920 lang=cpp
 *
 * [920] Number of Music Playlists
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int numMusicPlaylists(int n, int goal, int k) {
        long long MOD = 1000000007;
        std::vector<std::vector<long long>> dp(goal + 1, std::vector<long long>(n + 1, 0));
        dp[0][0] = 1;
        
        for (int j = 1; j <= n; j++) {
            for (int i = j; i <= goal; i++) {
                if (i > 0 && j > 0) {
                    dp[i][j] += dp[i - 1][j - 1] * (n - j + 1);
                    dp[i][j] %= MOD;
                }
                if (i > 0) {
                    dp[i][j] += dp[i - 1][j] * std::max(j - k, 0);
                    dp[i][j] %= MOD;
                }
            }
        }
        
        return static_cast<int>(dp[goal][n]);
    }
};
// @lc code=end

