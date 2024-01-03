/*
 * @lc app=leetcode id=2125 lang=cpp
 *
 * [2125] Number of Laser Beams in a Bank
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
    Remove all rows with "0" * n
    Then for two consecutive rows, add multiples of counts together
    */
    int numberOfBeams(std::vector<std::string>& bank) {
        int prev = 0, result = 0;
        for (const auto& row : bank) {
            int cur = std::count(row.begin(), row.end(), '1');
            if (cur == 0) continue;
            result += prev * cur;
            prev = cur;
        }
        return result;
    }
};

// @lc code=end

