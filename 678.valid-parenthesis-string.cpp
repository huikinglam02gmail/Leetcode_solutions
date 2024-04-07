/*
 * @lc app=leetcode id=678 lang=cpp
 *
 * [678] Valid Parenthesis String
 */

// @lc code=start
#include <string>
#include <algorithm>

class Solution {
public:
    bool checkValidString(std::string s) {
        int openMax = 0;
        int openMin = 0;
        for (char c : s) {
            if (c == '(') {
                openMax++;
                openMin++;
            }
            if (c == ')') {
                openMax--;
                openMin--;
            }
            if (c == '*') {
                openMax++;
                openMin--;
            }
            if (openMax < 0) {
                return false;
            }
            openMin = std::max(0, openMin);
        }
        return openMin == 0;
    }
};

// @lc code=end

