/*
 * @lc app=leetcode id=931 lang=cpp
 *
 * [931] Minimum Falling Path Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * DP problem
     * dp[i][j] = minimum path sum to arrive at [i,j]
     * dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) 
     */
    int minFallingPathSum(std::vector<std::vector<int>>& matrix) {
        int n = matrix.size();
        
        // Initialize the first row of dp
        std::vector<int> dp(matrix[0].begin(), matrix[0].end());
        
        for (int i = 1; i < n; ++i) {
            std::vector<int> dpNew(matrix[i].begin(), matrix[i].end());
            for (int j = 0; j < n; ++j) {
                if (j == 0) {
                    dpNew[j] += std::min(dp[j], dp[j+1]);
                } else if (j == n - 1) {
                    dpNew[j] += std::min(dp[j], dp[j-1]);
                } else {
                    dpNew[j] += std::min({dp[j-1], dp[j], dp[j+1]});
                }
            }
            dp = dpNew;
        }
        
        // Find the minimum value in the last row of dp
        return *std::min_element(dp.begin(), dp.end());
    }
};

// @lc code=end

