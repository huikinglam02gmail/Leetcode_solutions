/*
 * @lc app=leetcode id=2008 lang=cpp
 *
 * [2008] Maximum Earnings From Taxi
 */

// @lc code=start
#include <vector>
#include <algorithm>

using std::make_pair;
using std::max;
using std::pair;
using std::vector;

class Solution {
public:
    /*
    Solve the problem with DP
    dp[i] = maximum number of dollars you can earn by picking up the passengers optimally when you are at i + 1.
    we look for dp[n - 1]
    dp[i] = max(dp[i - 1], dp[i - j] + i - j + tips)
    */
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        vector<vector<pair<int, int>>> possibleEarnings(n);

        for (auto& ride : rides)
        {
            int s = ride[0];
            int e = ride[1];
            int t = ride[2];
            possibleEarnings[e - 1].push_back(make_pair(s - 1, t));
        }

        vector<long long> dp(n, (long long)0);
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i - 1];
            for (pair<int, int> pE : possibleEarnings[i]) {
                int s = pE.first;
                int t = pE.second;
                dp[i] = max(dp[i], dp[s] + (long long)(i - s + t));
            }
        }

        return dp[n - 1];
    }
};

// @lc code=end

