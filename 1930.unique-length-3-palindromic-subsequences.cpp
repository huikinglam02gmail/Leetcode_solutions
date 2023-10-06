/*
 * @lc app=leetcode id=1930 lang=cpp
 *
 * [1930] Unique Length-3 Palindromic Subsequences
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int countPalindromicSubsequence(std::string s) {
        std::vector<std::vector<int>> occur(26);

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            occur[c - 'a'].push_back(i);
        }

        int result = 0;

        for (int i = 0; i < 26; i++) {
            if (occur[i].size() > 1) {
                std::vector<int> startIndices = occur[i];
                int first = startIndices.front();
                int last = startIndices.back();

                for (int j = 0; j < 26; j++) {
                    auto left = std::upper_bound(occur[j].begin(), occur[j].end(), first);
                    auto right = std::lower_bound(occur[j].begin(), occur[j].end(), last);

                    if (left != right) {
                        result++;
                    }
                }
            }
        }

        return result;
    }
};

// @lc code=end

