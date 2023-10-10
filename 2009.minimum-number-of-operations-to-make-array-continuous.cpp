/*
 * @lc app=leetcode id=2009 lang=cpp
 *
 * [2009] Minimum Number of Operations to Make Array Continuous
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        nums.erase(std::unique(nums.begin(), nums.end()), nums.end());
        int result = INT_MAX;

        for (int i = 0; i < nums.size(); ++i) {
            int target = nums[i] + n - 1;
            int endIndex = std::upper_bound(nums.begin(), nums.end(), target) - nums.begin() - 1;
            int operations = n - (endIndex - i + 1);
            result = std::min(result, operations);
        }

        return result;
    }
};

// @lc code=end

