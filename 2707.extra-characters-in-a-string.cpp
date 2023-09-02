/*
 * @lc app=leetcode id=2707 lang=cpp
 *
 * [2707] Extra Characters in a String
 */

// @lc code=start
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int minExtraChar(std::string s, std::vector<std::string>& dictionary) {
        std::unordered_set<std::string> dictionarySet;
        for (const std::string& word : dictionary) {
            dictionarySet.insert(word);
        }

        int n = s.length();
        std::vector<int> dp(n + 1, n);
        dp[n] = 0;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j <= n; j++) {
                if (dictionarySet.find(s.substr(i, j - i)) == dictionarySet.end()) {
                    dp[i] = std::min(dp[i], j - i + dp[j]);
                } else {
                    dp[i] = std::min(dp[i], dp[j]);
                }
            }
        }

        return dp[0];
    }
};

// @lc code=end

