/*
 * @lc app=leetcode id=1624 lang=cpp
 *
 * [1624] Largest Substring Between Two Equal Characters
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxLengthBetweenEqualCharacters(std::string s) {
        std::vector<std::vector<int>> occur(26);

        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            occur[c - 'a'].push_back(i);
        }

        int result = -1;

        for (int i = 0; i < 26; i++) {
            if (!occur[i].empty()) {
                result = std::max(result, occur[i].back() - occur[i][0] - 1);
            }
        }

        return result;
    }
};

// @lc code=end

