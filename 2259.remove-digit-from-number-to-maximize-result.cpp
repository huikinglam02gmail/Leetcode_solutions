/*
 * @lc app=leetcode id=2259 lang=cpp
 *
 * [2259] Remove Digit From Number to Maximize Result
 */

// @lc code=start
#include <string>

class Solution {
public:
    std::string removeDigit(std::string number, char digit) {
        std::string result = "";
        int n = number.length();
        for (int i = 0; i < n; i++) {
            if (number[i] == digit) {
                result = result.compare(number.substr(0, i) + number.substr(i + 1)) > 0
                    ? result
                    : number.substr(0, i) + number.substr(i + 1);
            }
        }
        return result;
    }
};

// @lc code=end

