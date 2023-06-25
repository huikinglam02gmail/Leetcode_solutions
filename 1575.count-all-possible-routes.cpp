/*
 * @lc app=leetcode id=1575 lang=cpp
 *
 * [1575] Count All Possible Routes
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::vector;
using std::abs;
class Solution {
public:
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        int n = locations.size();
        long long MOD = 1000000007;
        vector<vector<int>> cost {};
        for (int i = 0; i < n; i++) {
            cost.push_back(vector<int>{});
            for (int j = 0; j < n; j++) {
                cost[i].push_back(abs(locations[i] - locations[j]));
            }
        }

        vector<vector<long long>> dp(n, vector<long long>(fuel + 1, 0));
        dp[start][fuel] = 1;

        for (int f = fuel; f >= 0; f--) {
            for (int i = 0; i < n; i++) {
                if (dp[i][f] > 0) {
                    for (int j = 0; j < n; j++) {
                        if (j != i && f - cost[i][j] >= 0) {
                            dp[j][f - cost[i][j]] += dp[i][f];
                            dp[j][f - cost[i][j]] %= MOD;
                        }
                    }
                }
            }
        }

        long long sum = 0;
        for (int i = 0; i <= fuel; i++)
        {
            sum += dp[finish][i];
            sum %= MOD;
        }

        return (int)sum;
    }
};
// @lc code=end

