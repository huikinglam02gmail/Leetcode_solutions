/*
 * @lc app=leetcode id=1143 lang=cpp
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * Classic DP problem
     * dp[i][j] = LCS length between text1[:i] and text2[:j]
     */
    int longestCommonSubsequence(std::string text1, std::string text2) {
        std::vector<std::vector<int>> dp(text2.length() + 1, std::vector<int>(text1.length() + 1, 0));

        for (int i = 1; i <= text2.length(); i++) {
            for (int j = 1; j <= text1.length(); j++) {
                dp[i][j] = std::max(dp[i][j - 1], dp[i - 1][j]);
                if (text1[j - 1] == text2[i - 1]) {
                    dp[i][j] = std::max(dp[i][j], dp[i - 1][j - 1] + 1);
                }
            }
        }

        return dp[text2.length()][text1.length()];
    }
};

// @lc code=end

