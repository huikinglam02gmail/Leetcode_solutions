/*
 * @lc app=leetcode id=2864 lang=cpp
 *
 * [2864] Maximum Odd Binary Number
 */

// @lc code=start
#include <string>

class Solution {
public:
    std::string maximumOddBinaryNumber(std::string s) {
        int n = s.size();
        int countOne = 0;
        for (char c : s) {
            if (c == '1') {
                countOne++;
            }
        }
        return std::string(countOne - 1, '1') + std::string(n - countOne, '0') + '1';
    }
};

// @lc code=end

