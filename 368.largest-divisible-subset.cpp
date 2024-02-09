/*
 * @lc app=leetcode id=368 lang=cpp
 *
 * [368] Largest Divisible Subset
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> largestDivisibleSubset(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> dp(nums.size(), std::vector<int>());

        for (int i = 0; i < nums.size(); ++i) {
            dp[i].push_back(nums[i]);
        }

        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && dp[i].size() < dp[j].size() + 1) {
                    dp[i] = dp[j];
                    dp[i].push_back(nums[i]);
                }
            }
        }

        int index = 0;
        int maxLength = 1;
        for (int i = 0; i < dp.size(); ++i) {
            if (dp[i].size() > maxLength) {
                index = i;
                maxLength = dp[i].size();
            }
        }

        return dp[index];
    }
};

// @lc code=end

