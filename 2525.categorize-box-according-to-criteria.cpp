/*
 * @lc app=leetcode id=2525 lang=cpp
 *
 * [2525] Categorize Box According to Criteria
 */

// @lc code=start
#include <string>

class Solution {
public:
    /**
     * Set bulky and heavy as booleans
     */
    std::string categorizeBox(int length, int width, int height, int mass) {
        bool bulky = length >= 10000 || width >= 10000 || height >= 10000 || (long long)length * (long long)width * (long long)height >= (long long)1000000000;
        bool heavy = mass >= 100;
        
        if (bulky && heavy) {
            return "Both";
        } else if (bulky) {
            return "Bulky";
        } else if (heavy) {
            return "Heavy";
        } else {
            return "Neither";
        }
    }
};

// @lc code=end

