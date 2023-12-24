/*
 * @lc app=leetcode id=1758 lang=cpp
 *
 * [1758] Minimum Changes To Make Alternating Binary String
 */

// @lc code=start
#include <string>
#include <cmath>

class Solution {
public:
    int minOperations(std::string s) {
        int S[2] = {0, 0};
        for (int i = 0; i < s.length(); i++) {
            S[1 - i % 2 - (int)std::pow(-1, i % 2) * (s[i] - '0')]++;
        }
        return std::min(S[0], S[1]);
    }
};

// @lc code=end

