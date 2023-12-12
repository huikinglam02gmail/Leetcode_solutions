/*
 * @lc app=leetcode id=1464 lang=cpp
 *
 * [1464] Maximum Product of Two Elements in an Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    // Sort then return product of top 2 -1
    int maxProduct(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        return (nums[nums.size() - 1] - 1) * (nums[nums.size() - 2] - 1);
    }
};

// @lc code=end

