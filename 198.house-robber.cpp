/*
 * @lc app=leetcode id=198 lang=cpp
 *
 * [198] House Robber
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * DP problem: dp[i] = the maximum amount of money you can rob tonight without alerting the police, given nums[:i + 1]
     * Recurrence relation quite simple: dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])   
     */
    int rob(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        } else if (n == 2) {
            return std::max(nums[0], nums[1]);
        } else {
            std::vector<int> dp(n, 0);
            dp[0] = nums[0];
            dp[1] = std::max(nums[0], nums[1]);
            for (int i = 2; i < n; ++i) {
                dp[i] = std::max(nums[i] + dp[i - 2], dp[i - 1]);
            }
            return dp[n - 1];
        }
    }
};

// @lc code=end

