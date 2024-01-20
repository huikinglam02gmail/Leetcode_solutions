/*
 * @lc app=leetcode id=2544 lang=cpp
 *
 * [2544] Alternating Digit Sum
 */

// @lc code=start
#include <string>

class Solution {
public:
    int alternateDigitSum(int n) {
        int result = 0;
        int sign = 1;

        for (char c : std::to_string(n)) {
            result += sign * (c - '0');
            sign *= -1;
        }

        return result;
    }
};

// @lc code=end

