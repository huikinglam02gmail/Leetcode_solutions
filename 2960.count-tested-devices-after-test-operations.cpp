/*
 * @lc app=leetcode id=2960 lang=cpp
 *
 * [2960] Count Tested Devices After Test Operations
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int countTestedDevices(std::vector<int>& batteryPercentages) {
        int result = 0;
        int deducted = 0;
        int i = 0;
        while (i < batteryPercentages.size()) {
            if (batteryPercentages[i] - deducted > 0) {
                result++;
                deducted++;
            }
            i++;
        }
        return result;
    }
};

// @lc code=end

