/*
 * @lc app=leetcode id=2239 lang=cpp
 *
 * [2239] Find Closest Number to Zero
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int findClosestNumber(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int x, int y) {
            return std::abs(x) == std::abs(y) ? x > y : std::abs(x) < std::abs(y);
        });

        return nums[0];
    }
};

// @lc code=end

