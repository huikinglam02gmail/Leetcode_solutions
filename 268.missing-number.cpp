/*
 * @lc app=leetcode id=268 lang=cpp
 *
 * [268] Missing Number
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int missingNumber(std::vector<int>& nums) {
        int defaultSum = nums.size() * (nums.size() + 1) / 2;
        for (int num : nums) {
            defaultSum -= num;
        }
        return defaultSum;
    }
};

// @lc code=end

