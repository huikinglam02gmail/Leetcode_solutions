/*
 * @lc app=leetcode id=1913 lang=cpp
 *
 * [1913] Maximum Product Difference Between Two Pairs
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProductDifference(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        return nums[nums.size() - 1] * nums[nums.size() - 2] - nums[0] * nums[1];
    }
};

// @lc code=end

