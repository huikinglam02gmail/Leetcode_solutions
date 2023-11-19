/*
 * @lc app=leetcode id=940 lang=cpp
 *
 * [940] Distinct Subsequences II
 */

// @lc code=start
#include <vector>
#include <numeric>
#include <string>

class Solution {
public:
    int distinctSubseqII(std::string s) {
        std::vector<long long> dp(26, (long long)0);
        long long current = 0;
        const long long MOD = (long long)1000000007;

        for (char c : s) {
            dp[c - 'a'] = (1 + current) % MOD;
            current = std::accumulate(dp.begin(), dp.end(), 0, [&](int sum, int val) {
                return (sum + val) % MOD;
            });
        }

        return (int)current;
    }
};

// @lc code=end

