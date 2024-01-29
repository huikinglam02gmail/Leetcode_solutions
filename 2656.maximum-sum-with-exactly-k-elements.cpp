/*
 * @lc app=leetcode id=2656 lang=cpp
 *
 * [2656] Maximum Sum With Exactly K Elements 
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int maximizeSum(std::vector<int>& nums, int k) {
        return *std::max_element(nums.begin(), nums.end()) * k + k * (k - 1) / 2;
    }
};

// @lc code=end

