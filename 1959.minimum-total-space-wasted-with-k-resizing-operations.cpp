/*
 * @lc app=leetcode id=1959 lang=cpp
 *
 * [1959] Minimum Total Space Wasted With K Resizing Operations
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int minSpaceWastedKResizing(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<int> prefix(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        std::vector<std::vector<int>> rangeMax(n, std::vector<int>(n, 0));
        std::vector<std::vector<int>> cost(n, std::vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (j == i) {
                    rangeMax[i][j] = nums[i];
                } else {
                    rangeMax[i][j] = std::max(nums[j], rangeMax[i][j - 1]);
                }
                cost[i][j] = (j + 1 - i) * rangeMax[i][j] - prefix[j + 1] + prefix[i];
            }
        }

        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n, INT_MAX));

        for (int i = 0; i <= k; i++) {
            dp[i][n - 1] = cost[n - 1][n - 1];
        }

        for (int i = 0; i <= k; i++) {
            for (int j = n - 2; j >= 0; j--) {
                if (i == 0) {
                    dp[i][j] = cost[j][n - 1];
                } else {
                    for (int l = j + 1; l <= n; l++) {
                        if (l < n) {
                            dp[i][j] = std::min(dp[i][j], dp[i - 1][l] + cost[j][l - 1]);
                        } else {
                            dp[i][j] = std::min(dp[i][j], cost[j][n - 1]);
                        }
                    }
                }
            }
        }

        return dp[k][0];
    }
};

// @lc code=end

