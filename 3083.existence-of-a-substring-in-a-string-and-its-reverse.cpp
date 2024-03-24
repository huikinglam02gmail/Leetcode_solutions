/*
 * @lc app=leetcode id=3083 lang=cpp
 *
 * [3083] Existence of a Substring in a String and Its Reverse
 */

// @lc code=start
#include <string>
#include <algorithm>

class Solution {
public:
    bool isSubstringPresent(std::string s) {
        std::string sReverse = s;
        std::reverse(sReverse.begin(), sReverse.end());
        int n = s.size();
        for (int i = 0; i < n - 1; i++) {
            std::string substr = s.substr(i, 2);
            if (sReverse.find(substr) != std::string::npos) {
                return true;
            }
        }
        return false;
    }
};

// @lc code=end

