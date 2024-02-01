/*
 * @lc app=leetcode id=2729 lang=cpp
 *
 * [2729] Check if The Number is Fascinating
 */

// @lc code=start
#include <string>
#include <algorithm>

class Solution {
public:
    bool isFascinating(int n) {
        std::string resultString;
        for (int i = 1; i <= 3; i++) {
            resultString += std::to_string(i * n);
        }
        for (int i = 1; i <= 9; i++) {
            if (std::count(resultString.begin(), resultString.end(), i + '0') != 1) {
                return false;
            }
        }
        return true;
    }
};

// @lc code=end

