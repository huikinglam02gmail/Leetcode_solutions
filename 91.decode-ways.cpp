/*
 * @lc app=leetcode id=91 lang=cpp
 *
 * [91] Decode Ways
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    int numDecodings(std::string s) {
        int n = s.length();
        if (s[0] == '0') return 0;

        std::vector<std::vector<int>> dp(2, std::vector<int>(n, 0));
        dp[0][0] = 1;

        for (int i = 1; i < n; i++) {
            if (s[i] == '0') {
                if (s[i - 1] == '1' || s[i - 1] == '2') {
                    dp[1][i] += dp[0][i - 1];
                }
            } else {
                dp[0][i] = dp[0][i - 1] + dp[1][i - 1];
                if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] >= '1' && s[i] <= '6')) {
                    if (i == 1) {
                        dp[1][i] = 1;
                    } else {
                        dp[1][i] = dp[1][i - 2] + dp[0][i - 2];
                    }
                }
            }
        }

        return dp[0][n - 1] + dp[1][n - 1];
    }
};

// @lc code=end

