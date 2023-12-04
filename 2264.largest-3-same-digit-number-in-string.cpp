/*
 * @lc app=leetcode id=2264 lang=cpp
 *
 * [2264] Largest 3-Same-Digit Number in String
 */

// @lc code=start
#include <string>

class Solution {
public:
    /**
     * Find "999" to "000" in num    
     */
    std::string largestGoodInteger(std::string num) {
        for (int i = 9; i >= 0; i--) {
            std::string search(3, static_cast<char>(i + '0'));
            if (num.find(search) != std::string::npos) return search;
        }
        return "";
    }
};

// @lc code=end

