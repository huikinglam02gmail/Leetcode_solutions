/*
 * @lc app=leetcode id=446 lang=cpp
 *
 * [446] Arithmetic Slices II - Subsequence
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    int numberOfArithmeticSlices(std::vector<int>& nums) {
        int n = nums.size();
        if (n < 3) {
            return 0;
        }

        std::vector<std::unordered_map<long long, int>> dp(n);
        int result = 0;

        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                long long diff = static_cast<long long>(nums[i]) - static_cast<long long>(nums[j]);

                // Add all previous elements as the first step
                dp[i][diff] += 1;

                // Look for longer subsequence
                if (dp[j].find(diff) != dp[j].end()) {
                    dp[i][diff] += dp[j][diff];
                    result += dp[j][diff];
                }
            }
        }

        return result;
    }
};

// @lc code=end

