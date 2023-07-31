/*
 * @lc app=leetcode id=712 lang=cpp
 *
 * [712] Minimum ASCII Delete Sum for Two Strings
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

class Solution {
public:
    /*
     * Classic DP string comparison problem
     * Build a 2D dp between the strings, with an extra position for the empty character
     * dp[i][j] = the lowest ASCII sum of deleted characters to make s1[:j] and s2[:i] equal.
     * The recursion formula is simple:
     * if s1[i] == s2[j]: dp[i][j] = dp[i-1][j-1]
     * else: dp[i][j] = min((int)s2[i] + dp[i-1][j], (int)s1[j] + dp[i][j-1])
     */
    int minimumDeleteSum(std::string s1, std::string s2) {
        int m = s2.length();
        int n = s1.length();
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, INT_MAX));

        dp[0][0] = 0;
        for (int i = 1; i <= n; i++)
            dp[0][i] = dp[0][i - 1] + static_cast<int>(s1[i - 1]);

        for (int i = 1; i <= m; i++)
            dp[i][0] = dp[i - 1][0] + static_cast<int>(s2[i - 1]);

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = std::min(dp[i][j], dp[i - 1][j] + static_cast<int>(s2[i - 1]));
                dp[i][j] = std::min(dp[i][j], dp[i][j - 1] + static_cast<int>(s1[j - 1]));

                if (s2[i - 1] == s1[j - 1])
                    dp[i][j] = std::min(dp[i][j], dp[i - 1][j - 1]);
            }
        }

        return dp[m][n];
    }
};

// @lc code=end

