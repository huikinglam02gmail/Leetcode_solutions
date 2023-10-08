/*
 * @lc app=leetcode id=1937 lang=cpp
 *
 * [1937] Maximum Number of Points with Cost
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long maxPoints(vector<vector<int>>& points) {
        int m = points.size();
        int n = points[0].size();
        vector<long> dp(points[0].begin(), points[0].end());

        for (int i = 0; i < m - 1; i++) {
            vector<long> dpNew(points[i + 1].begin(), points[i + 1].end());
            for (int j = n - 2; j >= 0; j--) {
                dp[j] = max(dp[j], dp[j + 1] - 1);
            }

            for (int j = 0; j < n; j++) {
                if (j > 0) {
                    dp[j] = max(dp[j], dp[j - 1] - 1);
                }

                dpNew[j] += dp[j];
            }
            dp = dpNew;
        }

        long maxPoints = *max_element(dp.begin(), dp.end());
        return maxPoints;
    }
};

// @lc code=end

