/*
 * @lc app=leetcode id=1987 lang=cpp
 *
 * [1987] Number of Unique Good Subsequences
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

class Solution {
public:
    int numberOfUniqueGoodSubsequences(std::string binary) {
        std::vector<long long> dp(2, (long long)0);
        long long current = 0;
        const long long MOD = 1000000007;
        int add1 = 0;

        for (char c : binary) {
            dp[c - '0'] = (c - '0' + current) % MOD;
            current = std::accumulate(dp.begin(), dp.end(), 0, [&](long long sum, long long val) {
                return (sum + val) % MOD;
            });
            if (c == '0') {
                add1 = 1;
            }
        }

        return (int)current + add1;
    }
};

// @lc code=end

