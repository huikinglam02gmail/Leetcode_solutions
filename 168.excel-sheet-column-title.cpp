/*
 * @lc app=leetcode id=168 lang=cpp
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
#include <string>

class Solution {
public:
    std::string convertToTitle(int columnNumber) {
        std::string result = "";
        while (columnNumber > 0) {
            result += static_cast<char>((columnNumber - 1) % 26 + 'A');
            columnNumber = (columnNumber - 1) / 26;
        }
        std::reverse(result.begin(), result.end());
        return result;
    }
};

// @lc code=end

