/*
 * @lc app=leetcode id=3065 lang=cpp
 *
 * [3065] Minimum Operations to Exceed Threshold Value I
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        return std::lower_bound(nums.begin(), nums.end(), k) - nums.begin();
    }
};

// @lc code=end

