/*
 * @lc app=leetcode id=2678 lang=cpp
 *
 * [2678] Number of Senior Citizens
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    int countSeniors(std::vector<std::string>& details) {
        int result = 0;
        for (const std::string& detail : details) {
            if (std::stoi(detail.substr(11, 2)) > 60) {
                result++;
            }
        }
        return result;
    }
};

// @lc code=end

