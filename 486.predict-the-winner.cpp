/*
 * @lc app=leetcode id=486 lang=cpp
 *
 * [486] Predict the Winner
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
     * Use DP to find the winner.
     * dp[i][j] = maximum score difference between player 1 and player 2 if nums[i:j + 1] is left behind and it's player 1's turn.
     */
    bool PredictTheWinner(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

        for (int j = 0; j < n; j++) {
            for (int i = j; i >= 0; i--) {
                if (i == j) {
                    dp[i][j] = nums[i];
                } else {
                    dp[i][j] = std::max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
                }
            }
        }

        return dp[0][n - 1] >= 0;
    }
};

// @lc code=end

