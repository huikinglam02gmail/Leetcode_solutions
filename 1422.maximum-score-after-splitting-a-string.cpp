/*
 * @lc app=leetcode id=1422 lang=cpp
 *
 * [1422] Maximum Score After Splitting a String
 */

// @lc code=start
#include <algorithm>

class Solution {
public:
    int maxScore(std::string s) {
        int n = s.length();
        int totalZeros = std::count(s.begin(), s.end(), '0');
        int totalOnes = n - totalZeros;
        int score = 0, zeros = 0;

        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == '0') {
                zeros += 1;
            }
            score = std::max(score, zeros + totalOnes - (i + 1 - zeros));
        }

        return score;
    }
};

// @lc code=end

