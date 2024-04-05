/*
 * @lc app=leetcode id=1544 lang=cpp
 *
 * [1544] Make The String Great
 */

// @lc code=start
#include <string>
#include <cmath>

class Solution {
public:
    std::string makeGood(std::string s) {
        std::string result;
        for (char c : s) {
            if (!result.empty() && std::abs(static_cast<int>(c) - static_cast<int>(result.back())) == 32) {
                result.pop_back();
            } else {
                result.push_back(c);
            }
        }
        return result;
    }
};

// @lc code=end

