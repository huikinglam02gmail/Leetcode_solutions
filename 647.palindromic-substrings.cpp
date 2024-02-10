/*
 * @lc app=leetcode id=647 lang=cpp
 *
 * [647] Palindromic Substrings
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    int countSubstrings(std::string s) {
        int n = s.length();
        std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));
        int count = 0;

        for (int j = 0; j < n; ++j) {
            for (int i = j; i >= 0; --i) {
                dp[i][j] = s[i] == s[j];
                if (i + 1 >= 0 && j - 1 >= 0 && i + 1 <= j - 1) {
                    dp[i][j] = dp[i][j] && dp[i + 1][j - 1];
                }
                if (dp[i][j]) {
                    ++count;
                }
            }
        }

        return count;
    }
};

// @lc code=end

