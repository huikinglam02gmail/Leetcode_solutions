/*
 * @lc app=leetcode id=2742 lang=cpp
 *
 * [2742] Painting the Walls
 */

// @lc code=start

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n = cost.size();
        vector<int> dp(n + 1, 500000001);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = n; j > 0; j--) {
                dp[j] = min(dp[j], dp[max(0, j - time[i] - 1)] + cost[i]);
            }
        }

        return dp[n];
    }
};

// @lc code=end

