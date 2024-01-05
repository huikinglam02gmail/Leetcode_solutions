/*
 * @lc app=leetcode id=300 lang=cpp
 *
 * [300] Longest Increasing Subsequence
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        std::vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            if (result.empty() || nums[i] > result.back()) {
                result.push_back(nums[i]);
            } else if (nums[i] < result.back()) {
                int index = std::lower_bound(result.begin(), result.end(), nums[i]) - result.begin();
                result[index] = nums[i];
            }
        }
        return result.size();
    }
};

// @lc code=end

