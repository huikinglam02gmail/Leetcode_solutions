/*
 * @lc app=leetcode id=2900 lang=cpp
 *
 * [2900] Longest Unequal Adjacent Groups Subsequence I
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> getLongestSubsequence(std::vector<std::string>& words, std::vector<int>& groups) {
        std::vector<std::vector<std::string>> results(2, std::vector<std::string>());
        for (int i = 0; i < words.size(); i++) {
            std::string word = words[i];
            int group = groups[i];
            if (results[group].size() % 2 == 0) {
                results[group].push_back(word);
            }
            if (results[1 - group].size() % 2 != 0) {
                results[1 - group].push_back(word);
            }
        }
        return results[0].size() >= results[1].size() ? results[0] : results[1];
    }
};

// @lc code=end

