/*
 * @lc app=leetcode id=1289 lang=cpp
 *
 * [1289] Minimum Falling Path Sum II
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    /*
    dp[i][j] = minimum of all falling path which ends at row i and column j
    Then we can just iterate through the rows from top to bottom    
    */
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        if (n == 1) {
            return grid[0][0];
        }
        
        vector<vector<int>> dp;
        for (int i = 0; i < n; i++) {
            vector<vector<int>> dpNew;
            if (i == 0) {
                for (int j = 0; j < n; j++) {
                    dpNew.push_back({grid[i][j], j});
                }
            } else {
                for (int j = 0; j < n; j++) {
                    if (j != dp[0][1]) {
                        dpNew.push_back({grid[i][j] + dp[0][0], j});
                    } else {
                        dpNew.push_back({grid[i][j] + dp[1][0], j});
                    }
                }
            }
            dp = dpNew;
            sort(dp.begin(), dp.end(), [](const vector<int>& a, const vector<int>& b) {
                return a[0] < b[0];
            });
        }
        
        return dp[0][0];
    }
};

// @lc code=end

